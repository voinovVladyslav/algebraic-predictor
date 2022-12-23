from app.api import api
from . import views


api.add_resource(
    views.ProjectView, '/api/projects/create', endpoint='project-create',
)
