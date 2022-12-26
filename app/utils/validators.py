from app.api.errors import (
    FieldMissingError,
    TooManyFieldsError,
)


def has_all_required_fields(json_data: dict):
    required_fields = {
        'email': None,
        'password': None,
    }
    required_fields_count = len(required_fields)
    required_fields.update(json_data)
    for v in required_fields.values():
        if not v:
            raise FieldMissingError
    if len(required_fields) != required_fields_count:
        raise TooManyFieldsError

    return True
