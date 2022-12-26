from flask import request
from flask_restful import Resource

from app.models import User
from app.utils.decorators import (
    auth_required,
    admin_only,
)
from app.api.errors import Errors


class UserCreate(Resource):
    def post(self):
        json_data: dict = request.get_json(force=True)

        result, error = User().has_all_required_fields(json_data)
        if error is not None:
            return error

        filter = {'email': json_data['email']}
        user = User().get_user(**filter)

        if not user:
            User().create_user(**json_data)
            return {'success': 'user created successfully'}
        return Errors.user_already_exists


class Users(Resource):
    @auth_required
    @admin_only
    def get(self, **kwargs):
        users = User().get_queryset()
        return users


class ObtainToken(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        result, error = User().has_all_required_fields(json_data)
        if not result:
            return error

        token = User().authenticate(
            json_data['email'],
            json_data['password'],
        )
        if not token:
            Errors.invalid_credentials
        return {'token': token}


class UserProfile(Resource):
    @auth_required
    def get(self, **kwargs):
        user = User().get_user(token=kwargs['token'])
        return user
