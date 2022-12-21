from flask import request
from flask_restful import Resource

from app.models import User


class UserCreate(Resource):
    def post(self):
        json_data: dict = request.get_json(force=True)

        if not self.has_all_required_fields(json_data):
            # to-do: return missing fields
            return {'error': 'invalid fields'}

        filter = {'username': json_data['username']}
        user = User().get_user(**filter)

        if not user:
            User().create_user(**json_data)
            return {'success': 'user created successfully'}

        return {'error': 'username is already taken'}

    @staticmethod
    def has_all_required_fields(json_data: dict):
        required_fields = {
            'username': None,
            'password': None,
        }
        required_fields_count = len(required_fields)
        required_fields.update(json_data)
        for v in required_fields.values():
            if not v:
                return False
        return len(required_fields) == required_fields_count


class Users(Resource):
    def get(self):
        users = User().get_queryset()
        return users
