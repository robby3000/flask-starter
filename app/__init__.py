from flask import Flask
from config import config
from .extensions import db, login_manager, bcrypt, csrf, htmx
import datetime

def create_app(config_name='default'):
    """Application factory function."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize Flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
    htmx.init_app(app)

    # Register blueprints
    # --- Main Blueprint --- #
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # --- Auth Blueprint --- #
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # Add context processors or other app-level configurations if needed
    @app.context_processor
    def inject_now():
        """Inject current UTC time into all templates."""
        return {'now': datetime.datetime.utcnow()}

    # @app.shell_context_processor
    # def make_shell_context():
    #     return dict(db=db, User=User) # Example context for 'flask shell'

    return app
