from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from htmx_flask import Htmx

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
csrf = CSRFProtect()
htmx = Htmx()

# Configure Flask-Login
login_manager.login_view = 'auth.login' # The route name for the login page
login_manager.login_message_category = 'info' # Flash message category

@login_manager.user_loader
def load_user(user_id):
    """User loader callback for Flask-Login."""
    # Import the User model here to avoid circular imports
    from .models import User
    return User.query.get(int(user_id))
