from flask import Blueprint
from . import users
from .users import User


models = Blueprint('models', __name__)
