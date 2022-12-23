from app.api import api
from . import views


api.add_resource(
    views.UserCreate, '/api/user/create', endpoint='user-create'
)
api.add_resource(
    views.ObtainToken, '/api/user/token', endpoint='user=token',
)
api.add_resource(
    views.UserProfile, '/api/user/me', endpoint='user-me',
)

# for admin
api.add_resource(
    views.Users, '/api/user/all', endpoint='user-all'
)
