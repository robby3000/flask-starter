from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .extensions import db, bcrypt

class User(UserMixin, db.Model):
    """User model for authentication."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # Flask-Login integration
    # UserMixin provides implementations for these properties and methods:
    # is_authenticated, is_active, is_anonymous, get_id()

    def set_password(self, password):
        """Hashes the password using bcrypt and stores it."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Checks if the provided password matches the stored hash."""
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
