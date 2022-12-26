from .base import BaseModel

from app.utils.hash import (
    secure_password,
    generate_token,
)
from app.utils.time import get_now_time


class User(BaseModel):
    def __init__(self):
        super().__init__()
        self.users = self.db.users
        self.required_fields = [
            'email',
            'password',
        ]

    def get_queryset(self, filter: dict = {}, fields: str = ''):
        return super()._get_queryset(self.users, filter, fields)

    def create_user(self, email, password):
        defaults = {
            'email': email,
            'password': secure_password(password),
            'date_joined': get_now_time(),
            'token': generate_token(),
            'is_admin': False,
        }
        self.users.insert_one(defaults)

    def create_admin(self, email, password):
        defaults = {
            'email': email,
            'password': secure_password(password),
            'date_joined': get_now_time(),
            'token': generate_token(),
            'is_admin': True,
        }
        self.users.insert_one(defaults)

    def get_user(self, **kwargs):
        result = self.get_queryset(kwargs)
        try:
            return result[0]
        except IndexError:
            return

    def authenticate(self, email, password):
        user = self.get_user(
            email=email,
            password=secure_password(password)
        )
        if not user:
            return None
        return user['token']

    def is_admin(self, token):
        user = self.get_user(token=token)
        return user.get('is_admin')

    def has_all_required_fields(self, json_data: dict):
        return super()._has_all_reqired_fields(
            self.required_fields,
            json_data,
        )
