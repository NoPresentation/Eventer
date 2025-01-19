Eventer - Event Management Web Application
This is a Flask-based web application for managing events. The application allows users to create, update, view, and delete events, with the added functionality of specifying the event's location and displaying its creation date. Event organizers can manage their own events after authentication, with access control ensuring that users can only interact with their own events.

Features:

1. User Authentication:
Users can sign up, log in, and log out.
Secure authentication system to protect user data and event information.

2. Event Management:
Create events with a title, description, and location.
Update event details (title, description, location) after creation.
Delete events with a confirmation prompt.

3. Event Details:
View detailed information about each event, including the event's title, description, location, and creation date.

4. User Permissions:
Only the event creator (user) can update or delete their event.
Users cannot access or modify events created by other users.

Installation:
- Prerequisites
    Python 3.11.9
    blinker==1.9.0
    click==8.1.8
    colorama==0.4.6
    Flask==3.1.0
    Flask-Login==0.6.3
    Flask-SQLAlchemy==3.1.1
    Flask-WTF==1.2.2
    greenlet==3.1.1
    itsdangerous==2.2.0
    Jinja2==3.1.5
    MarkupSafe==3.0.2
    SQLAlchemy==2.0.37
    typing_extensions==4.12.2
    Werkzeug==3.1.3
    WTForms==3.2.1

- Steps
1. Clone the repository:
git clone https://github.com/your-username/event-management-app.git

2. Create a virtual environment and activate it in your directory
python -m venv /path/to/new/virtual/environment

3. Install dependencies:
pip install -r req.txt

4. Run the application:
flask run
Open your browser and navigate to http://127.0.0.1:5000/.

Usage
Sign Up: Users can create an account by navigating to the registration page and providing a username and password.
Create Events: Once logged in, users can create new events by filling in a form with the event's title, description, and location.
Update Events: Users can edit event details after creation, such as title, description, and location.
Delete Events: Users can delete events with a confirmation prompt to prevent accidental deletions.
View Events: The event details page displays all relevant event information, including location and creation date.
Project Structure

Technologies Used
Flask: Web framework for Python.
Flask-SQLAlchemy: ORM for database management.
Flask-WTF: Form handling with Flask.
Flask-Login: User session management.