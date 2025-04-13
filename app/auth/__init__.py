from flask import Blueprint

auth = Blueprint('auth', __name__)

# Import routes and forms at the bottom
from . import routes, forms
