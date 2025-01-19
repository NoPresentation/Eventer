from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class EventForm(FlaskForm):
  title = StringField(label='Title', validators=[DataRequired()])
  location = StringField(label='Event Location', validators=[DataRequired()])
  description = TextAreaField(label='Description', validators=[DataRequired()])
  submit = SubmitField('Commit')


class LogInForm(FlaskForm):
  user_name = StringField(label='Username', validators=[DataRequired()])
  password = StringField(label='Password', validators=[DataRequired()])
  submit = SubmitField('Enter')