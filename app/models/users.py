from .base import BaseModel

from app.utils.hash import (
    secure_password,
    generate_token,
)
from app.utils.time import get_now_time


class User(BaseModel):
    def get_queryset(self):
        users = self.db.users.find(
            {},
            {
                '_id': 0,
            },
        )
        return list(users)

    def create_user(self, username, password):
        defaults = {
            'username': username,
            'password': secure_password(password),
            'date_joined': get_now_time(),
            'token': generate_token(),
            'is_admin': False,
        }
        self.db.users.insert_one(defaults)

    def create_admin(self, username, password):
        defaults = {
            'username': username,
            'password': secure_password(password),
            'date_joined': get_now_time(),
            'token': generate_token(),
            'is_admin': True,
        }
        self.db.users.insert_one(defaults)

    def get_user(self, **kwargs):
        result = list(self.db.users.find(kwargs))
        try:
            return result[0]
        except IndexError:
            return
