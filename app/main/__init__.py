from flask import Blueprint

main = Blueprint('main', __name__)

# Import routes and error handlers at the bottom to avoid circular dependencies
from . import routes #, errors
