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

    def get_queryset(self, args: str = ''):
        return super()._get_queryset(self.users, args)

    def create_user(self, username, password):
        defaults = {
            'username': username,
            'password': secure_password(password),
            'date_joined': get_now_time(),
            'token': generate_token(),
            'is_admin': False,
        }
        self.users.insert_one(defaults)

    def create_admin(self, username, password):
        defaults = {
            'username': username,
            'password': secure_password(password),
            'date_joined': get_now_time(),
            'token': generate_token(),
            'is_admin': True,
        }
        self.users.insert_one(defaults)

    def get_user(self, **kwargs):
        result = list(self.users.find(kwargs))
        try:
            return result[0]
        except IndexError:
            return

    def authenticate(self, username, password):
        user = self.get_user(
            username=username,
            password=secure_password(password)
        )
        if not user:
            return None
        return user['token']
