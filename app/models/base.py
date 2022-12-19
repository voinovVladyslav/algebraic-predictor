from abc import ABC
from app import mongo


class BaseModel(ABC):
    def __init__(self):
        self.db = mongo.db

    def get_queryset(self):
        pass
