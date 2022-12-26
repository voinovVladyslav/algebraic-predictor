from .base import BaseModel

from app.utils.time import get_now_time


class Project(BaseModel):
    def __init__(self):
        super().__init__()
        self.projects = self.db.projects
        self.required_fields = [
            'title',
        ]
        self.optional_fields = [
            'script',
            'environment',
        ]

    def get_queryset(self, filter: dict = {}, fields: str = ''):
        return super()._get_queryset(self.projects, filter, fields)

    def create(
            self,
            user_token: str,
            title: str,
            script: str = None,
            environment: str = None,
            ):

        result = self.projects.insert_one(
            {
                'user_token': user_token,
                'title': title,
                'script': script,
                'environment': environment,
                'date_created': get_now_time(),
                'last_updated': get_now_time(),
            }
        )
        return result

    def has_all_required_fields(self, json_data: dict):
        return super()._has_all_reqired_fields(
            self.required_fields,
            self.optional_fields,
            json_data,
        )
