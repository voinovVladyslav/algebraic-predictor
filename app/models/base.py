from abc import ABC
from app import mongo


class BaseModel(ABC):
    def __init__(self):
        self.db = mongo.db

    @staticmethod
    def _get_queryset(collection, args: str = ''):
        args = args.split()
        filter = {'_id': False}
        filter.update(
            {
                x[1:] if x.startswith('-') else x: not x.startswith('-')
                for x in args
            }
        )
        query = collection.find(
            {},
            filter
        )
        return list(query)
