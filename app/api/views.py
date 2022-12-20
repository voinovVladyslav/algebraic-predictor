from flask import request
from flask_restful import Resource

from app.models import User


class UserCreate(Resource):
    def post(self):
        json_data: dict = request.get_json(force=True)

        if not self.has_all_required_fields(json_data.copy()):
            # to-do: return missing fields
            return {'error': 'required field missing'}

        filter = {'username': json_data['username']}
        user = User().get_user(**filter)

        if not user:
            User().create_user(**json_data)
            return {'success': 'user created successfully'}

        return {'error': 'username is already taken'}

    @staticmethod
    def has_all_required_fields(json_data: dict):
        if not json_data.pop('username', None):
            return False
        if not json_data.pop('password', None):
            return False
        if json_data:
            return False
        return True


class Users(Resource):
    def get(self):
        users = User().get_queryset()
        return users
