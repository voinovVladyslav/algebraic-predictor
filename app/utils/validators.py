def has_all_required_fields(json_data: dict):
    required_fields = {
        'username': None,
        'password': None,
    }
    required_fields_count = len(required_fields)
    required_fields.update(json_data)
    for v in required_fields.values():
        if not v:
            return False
    return len(required_fields) == required_fields_count
