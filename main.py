from flask import Flask, url_for, redirect, session, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import EventForm, LogInForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'if_you_hack_me_you_will_be_hacked'
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)

    events = db.relationship('Event', backref='creator', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Event {self.title}, {self.date}'


# Routes
@app.route('/')
def home():
    if "user_id" in session:
        events = Event.query.filter_by(user_id = session['user_id']).all()
        return render_template('home.html', events=events)
    
    return redirect(url_for('login'))

# Login - Register - Logout routes
@app.route('/login', methods=['GET','POST'])
def login():
    loginform = LogInForm()

    if loginform.validate_on_submit():
        user = User.query.filter_by(user_name=loginform.user_name.data).first()
        if user and user.check_password(loginform.password.data):
            print("USER FOUND")
            session['user_id'] = user.id
            print(session.get('user_id'))
            return redirect(url_for('home'))

    error_message = 'Make sure the information you entered is correct, or create an account if you are not a user yet'
    return render_template('login.html', form=loginform, error_message=error_message)

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET','POST'])
def register():
    register_form = LogInForm()

    if register_form.validate_on_submit():
        user = User.query.filter_by(user_name = register_form.user_name.data).first()
        if user:
            redirect(url_for('login'))
        else:
            new_user = User()
            new_user.user_name = register_form.user_name.data
            new_user.set_password(register_form.password.data)
            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id
            return redirect(url_for('home'))
        
    return render_template('register.html', form = register_form)


# Create - Retrieve - Update - Delete routes
@app.route('/event/<int:event_id>')
def event_details(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event_details.html', event=event)


@app.route('/create', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(
            user_id=session.get('user_id'),
            title=form.title.data,
            location=form.location.data,
            description=form.description.data,
        )
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template('create_event.html', form=form)


@app.route('/update_event/<int:event_id>', methods=['GET', 'POST'])
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    form = EventForm(obj=event)
    form.submit.label.text = "Update Event"
    if form.validate_on_submit() and session['user_id'] == event.user_id:
        event.title = form.title.data
        event.location = form.location.data
        event.description = form.description.data
        db.session.commit()
        return redirect(url_for('event_details', event_id=event.id))
    
    return render_template('update_event.html', form=form, event=event)

@app.route('/delete/<int:event_id>')
def delete_event(event_id):
    event = Event.query.get(event_id)
    if event and session['user_id'] == event.user_id:
        db.session.delete(event)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('event_details', event)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
