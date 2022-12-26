from flask import request
from flask_restful import Resource

from app.models import Project
from app.utils.decorators import (
    auth_required,
    admin_only,
)


class ProjectListView(Resource):
    @auth_required
    def get(self, **kwargs):
        token = kwargs['token']
        projects = Project().get_queryset(
            {
                'user_token': token,
            }
        )
        return projects

    @auth_required
    def post(self, **kwargs):
        token = kwargs['token']
        json_data = request.get_json(force=True)
        Project().has_all_required_fields(json_data)
        Project().create(
            user_token=token,
            **json_data
        )
