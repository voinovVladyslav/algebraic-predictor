from abc import ABC
from app import mongo

from app.api.errors import Errors


class BaseModel(ABC):
    def __init__(self):
        self.db = mongo.db
        self.required_fields = []
        self.optional_fields = []

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

    @staticmethod
    def _has_all_reqired_fields(
            field_names: list,
            optional_field_names: list,
            json_data: dict
            ):
        required_fields = dict()
        for field_name in field_names:
            required_fields[field_name] = None

        required_fields.update(json_data)
        for v in required_fields.values():
            if v is None:
                return False, Errors.field_missing

        for key in json_data.keys():
            if (key not in optional_field_names
                    and key not in field_names):
                return False, Errors.too_many_fields

        return True, None

    def has_all_required_fields(json_data: dict):
        pass
