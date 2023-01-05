from .base import BaseModel

from app.utils.time import get_now_time
from app.api.errors import Errors


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

    def update(
        self,
        user_token: str,
        title: str,
        new_fields: dict
    ):
        update = dict(last_updated=get_now_time())
        new_fields.pop('date_created', None)
        new_fields.pop('last_updated', None)
        update.update(**new_fields)
        self.projects.update_one(
            {
                'user_token': user_token,
                'title': title,
            },
            {'$set': update}
        )

    def validate(self, json_data: dict):
        errors = super()._validate(
            self.required_fields,
            self.optional_fields,
            json_data,
        )
        if errors is not None:
            return errors
        return self._validate_title(json_data['title'])

    @staticmethod
    def _validate_title(title):
        if len(title.split()) != 1:
            return Errors.title_must_not_contain_spaces
        return

    def validate_patch(self, json_data: dict):
        errors = super()._validate(
            self.required_fields,
            self.optional_fields,
            json_data,
        )
        if errors is not None:
            return errors
        title = json_data.get('title', None)
        if not title:
            return
        return self._validate_title(json_data['title'])
