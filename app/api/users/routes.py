from app.api import api_app
from . import views


api_app.add_resource(
    views.UserCreate, '/api/user/create', endpoint='user-create'
)
api_app.add_resource(
    views.ObtainToken, '/api/user/token', endpoint='user=token',
)
api_app.add_resource(
    views.UserProfile, '/api/user/me', endpoint='user-me',
)

# for admin
api_app.add_resource(
    views.Users, '/api/user/all', endpoint='user-all'
)
