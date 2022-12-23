from abc import ABC
from app import mongo


class BaseModel(ABC):
    def __init__(self):
        self.db = mongo.db

    @staticmethod
    def _get_queryset(collection, filter: dict = {}, args: str = ''):
        args = args.split()
        fields = {'_id': False}
        fields.update(
            {
                x[1:] if x.startswith('-') else x: not x.startswith('-')
                for x in args
            }
        )
        query = collection.find(
            filter,
            fields
        )
        return list(query)

    def get_queryset(self, filter: dict = {}, args: dict = {}):
        pass
