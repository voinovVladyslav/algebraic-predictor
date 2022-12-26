from flask import request
from flask_restful import Resource

from app.models import User
from app.utils.validators import has_all_required_fields
from app.utils.decorators import (
    auth_required,
    admin_only,
)
from app.api.errors import (
    InvalidCredentialsError,
    UserAlreadyExistsError,
)


class UserCreate(Resource):
    def post(self):
        json_data: dict = request.get_json(force=True)

        has_all_required_fields(json_data)

        filter = {'email': json_data['email']}
        user = User().get_user(**filter)

        if not user:
            User().create_user(**json_data)
            return {'success': 'user created successfully'}
        raise UserAlreadyExistsError


class Users(Resource):
    @auth_required
    @admin_only
    def get(self):
        users = User().get_queryset()
        return users


class ObtainToken(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        has_all_required_fields(json_data)

        token = User().authenticate(
            json_data['email'],
            json_data['password'],
        )
        if not token:
            raise InvalidCredentialsError
        return {'token': token}


class UserProfile(Resource):
    @auth_required
    def get(self, **kwargs):
        user = User().get_user(token=kwargs['token'])
        return user
