from flask import request
from flask_restful import Resource

from app.models import User
from app.utils.validators import has_all_required_fields


class UserCreate(Resource):
    def post(self):
        json_data: dict = request.get_json(force=True)

        if not has_all_required_fields(json_data):
            # to-do: return missing fields
            return {'error': 'invalid fields'}

        filter = {'username': json_data['username']}
        user = User().get_user(**filter)

        if not user:
            User().create_user(**json_data)
            return {'success': 'user created successfully'}

        return {'error': 'username is already taken'}


class Users(Resource):
    def get(self):
        users = User().get_queryset()
        return users


class ObtainToken(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        if not has_all_required_fields(json_data):
            return {'error': 'invalid fields'}

        token = User().authenticate(
            json_data['username'],
            json_data['password'],
        )
        if not token:
            return {'error': 'invalid credentials'}
        return {'token': token}


class UserProfile(Resource):
    def get(self):
        # expected value: "Token 23rhifd23iufbeursrgd"
        token = request.headers.get('Token', None)
        if not token:
            return {'error': 'authentication required'}

        user = User().get_user(token=token.split()[1])
        if not user:
            return {'error': 'invalid credentials'}
        return user
