import os
from dotenv import load_dotenv

# Load environment variables from .env file
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """Base configuration settings."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Add other default configurations here

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db') # Default to SQLite if not set

    # Flask-Login configuration
    LOGIN_DISABLED = os.environ.get('LOGIN_DISABLED', 'False').lower() in ('true', '1', 't')

    # HTMX configuration
    HTMX_USE_CDN = False # We'll load it via webpack

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    """Development configuration settings."""
    DEBUG = True
    # Add development-specific configurations here
    # Example:SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    """Testing configuration settings."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://' # Use in-memory SQLite for tests
    WTF_CSRF_ENABLED = False # Disable CSRF forms protection in tests

class ProductionConfig(Config):
    """Production configuration settings."""
    # Add production-specific configurations here
    # Example: SQLALCHEMY_POOL_RECYCLE = 299
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
