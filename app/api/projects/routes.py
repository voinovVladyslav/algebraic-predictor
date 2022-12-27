from app.api import api_app
from . import views


api_app.add_resource(
    views.ProjectListView,
    '/api/projects/',
    endpoint='projects',
    methods=['GET', 'POST'],
)

api_app.add_resource(
    views.ProjectDetailView,
    '/api/projects/<project_title>/',
    endpoint='project',
    methods=['GET', 'PUT', 'PATCH', 'DELETE'],
)
