from flask import request
from flask_restful import Resource

from app.models import Project
from app.utils.decorators import (
    auth_required,
    admin_only,
)


class ProjectView(Resource):
    @auth_required
    def get(self, **kwargs):
        return {'project': 'endpoint'}
