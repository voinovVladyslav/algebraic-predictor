from flask import request
from flask_restful import Resource

from app import mongo
from app.models import User

from app.utils.hash import (
    secure_password,
    generate_token,
)
from app.utils.time import get_now_time


class UserCreate(Resource):
    def post(self):
        db = mongo.db
        json_data = request.get_json(force=True)

        if not self.has_all_required_fields(json_data):
            # to-do: return missing fields
            return {'error': 'required field missing'}

        filter = {'username': json_data['username']}
        user = db.users.find_one(filter=filter)

        if not user:
            password = secure_password(json_data['password'])
            db.users.insert_one({
                'username': json_data['username'],
                'password': password,
                'token': generate_token(),
                'date_joined': get_now_time(),
            })
            return {'success': 'user created successfully'}

        return {'error': 'username is already taken'}

    @staticmethod
    def has_all_required_fields(json_data):
        if not json_data.get('username', None):
            return False
        if not json_data.get('password', None):
            return False
        return True


class Users(Resource):
    def get(self):
        users = User().get_queryset()
        return list(users)
