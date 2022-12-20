from flask import Blueprint

from . import views
from . import routes


api = Blueprint('api', __name__)
