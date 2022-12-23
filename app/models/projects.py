from .base import BaseModel

from app.utils.time import get_now_time


class Projects(BaseModel):
    def __init__(self):
        super().__init__()
        self.projects = self.db.projects

    def get_queryset(self, filter: dict = {}, fields: str = ''):
        return super()._get_queryset(self.projects, filter, fields)
