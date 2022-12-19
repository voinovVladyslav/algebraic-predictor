from .base import BaseModel


class User(BaseModel):
    def get_queryset(self):
        users = self.db.users.find(
            {},
            {
                '_id': 0,
                'password': 0,
            },
        )
        return users
