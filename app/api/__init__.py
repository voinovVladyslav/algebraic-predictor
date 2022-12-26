from flask import Blueprint
from flask_restful import Api


api_bp = Blueprint('api', __name__)
api_app = Api(api_bp)


from .users import (
    routes as user_routes,
    views as user_views
)

from .projects import (
    routes as project_routes,
    views as project_views
)
