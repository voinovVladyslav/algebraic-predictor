from flask import Blueprint


models = Blueprint('models', __name__)


from . import users
from .users import User
