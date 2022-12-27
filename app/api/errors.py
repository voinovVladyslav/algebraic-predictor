class Errors:
    invalid_credentials = (
        {'error': 'Invalid credentials'},
        400
    )
    unauthorized = (
        {'error': 'Unauthorized'},
        401
    )
    permission_denied = (
        {'error': 'Permission denied'},
        403
    )
    field_missing = (
        {'error': 'Required field(s) missing'},
        400
    )
    too_many_fields = (
        {'error': 'Too many fields'},
        400
    )
    user_already_exists = (
        {'error': 'User already exists'},
        400
    )
    title_must_not_contain_spaces = (
        {'error': 'Field "title" must be continuous line '
                  'e.g. "my_title", not "my title"'},
        400
    )
