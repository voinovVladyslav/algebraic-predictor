from flask import request
from flask_restful import Resource

from app.models import Project
from app.utils.decorators import (
    auth_required,
)
from app.api.errors import Errors


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
        error = Project().validate(json_data)
        if error is not None:
            return error
        Project().create(
            user_token=token,
            **json_data
        )
        return {'ok': 'Created successfully'}


class ProjectDetailView(Resource):
    @auth_required
    def get(self, project_title, **kwargs):
        project = Project().get_queryset(
            {
                'user_token': kwargs['token'],
                'title': project_title,
            },
            '-user_token',
        )
        if not project:
            return Errors.not_found
        return project

    @auth_required
    def put(self, project_title, **kwargs):
        json_data = request.get_json(force=True)
        title = json_data.get('title', None)
        if title:
            errors = Project()._validate_title(title)
            if errors is not None:
                return errors

        Project().update(
            user_token=kwargs['token'],
            title=project_title,
            new_fields=json_data,
        )
        return {'ok': 'updated'}

    @auth_required
    def patch(self, project_title, **kwargs):
        json_data = request.get_json(force=True)
        errors = Project().validate_patch(
            json_data
        )
        if errors:
            return errors

        Project().update(
            user_token=kwargs['token'],
            title=project_title,
            new_fields=json_data,
        )
        return {'ok': 'updated'}


    @auth_required
    def delete(self, project_title, **kwargs):
        pass
