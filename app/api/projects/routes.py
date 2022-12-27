from app.api import api_app
from . import views


api_app.add_resource(
    views.ProjectListView,
    '/api/projects/',
    endpoint='projects',
    methods=['GET', 'POST'],
)
