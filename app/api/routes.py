from . import api as api_app
from flask_restful import Api
from . import views

api = Api(api_app)

api.add_resource(
    views.UserCreate, '/api/user/create', endpoint='user-create'
)
api.add_resource(
    views.ObtainToken, '/api/user/token', endpoint='user=token',
)

# for admin
api.add_resource(
    views.Users, '/api/user/all', endpoint='user-all'
)
