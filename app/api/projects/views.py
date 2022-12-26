from flask import request
from flask_restful import Resource

from app.models import Project
from app.utils.decorators import (
    auth_required,
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
        res, error = Project().has_all_required_fields(json_data)
        if not res:
            return error
        Project().create(
            user_token=token,
            **json_data
        )
        return {'ok': 'Created successfully'}
