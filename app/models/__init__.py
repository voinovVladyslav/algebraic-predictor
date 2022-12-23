from flask import Blueprint


models = Blueprint('models', __name__)


from . import users
from . import projects
from .users import User
from .projects import Project
