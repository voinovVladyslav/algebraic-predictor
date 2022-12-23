from .base import BaseModel

from app.utils.time import get_now_time


class Project(BaseModel):
    def __init__(self):
        super().__init__()
        self.projects = self.db.projects

    def get_queryset(self, filter: dict = {}, fields: str = ''):
        return super()._get_queryset(self.projects, filter, fields)

    def create(
            self,
            title: str,
            script: str = None,
            environment: str = None,
            user_token: str = None,
            ):

        result = self.projects.insert_one(
            {
                'title': title,
                'script': script,
                'environment': environment,
                'user_token': user_token,
                'date_created': get_now_time(),
                'last_updated': get_now_time(),
            }
        )
        return result
