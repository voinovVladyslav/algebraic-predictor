import hashlib
from datetime import datetime
from uuid import uuid4
from flask import request
from flask_restful import Resource

from app import mongo
from config import DevelopmentConfig
from app.models import User



class UserCreate(Resource):
    def post(self):
        db = mongo.db
        json_data = request.get_json(force=True)

        if not self.has_all_required_fields(json_data):
            return {'error': 'required field missing'} # to-do: return missing fields

        filter = {'username': json_data['username']}
        user = db.users.find_one(filter=filter)

        if not user:
            password_to_secure = json_data['password'] + DevelopmentConfig.SECRET_KEY
            hashed_passwd = hashlib.sha256(password_to_secure.encode()).hexdigest()
            db.users.insert_one({
                'username': json_data['username'],
                'password': hashed_passwd,
                'token': uuid4().hex,
                'date_joined': datetime.now().strftime('')
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
