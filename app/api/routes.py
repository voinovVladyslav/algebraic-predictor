from . import api as api_app
from flask_restful import Api
from . import views

api = Api(api_app)

api.add_resource(views.UserCreate, '/api/user/create', endpoint='user-create')
