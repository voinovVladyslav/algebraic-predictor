class InvalidCredentialsError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class PermissionDeniedError(Exception):
    pass


class InternalServerError(Exception):
    pass


class FieldMissingError(Exception):
    pass


class TooManyFieldsError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


errors = {
    'InvalidCredentialsError': {
        'error': 'Invalid credentials',
        'code': 400,
    },
    'UnauthorizedError': {
        'error': 'Authentication required',
        'code': 401,
    },
    'PermissionDeniedError': {
        'error': 'Not allowed',
        'code': 403,
    },
    'InternalServerError': {
        'error': 'Something went wrong',
        'code': 500,
    },
    'FieldError': {
        'error': 'Required field(s) missing',
        'code': 400,
    },
    'TooManyFieldsError': {
        'error': 'Too many fields',
        'code': 400,
    },
    'UserAlreadyExistsError': {
        'error': 'User with that email already exists',
        'code': 400,
    },
}
