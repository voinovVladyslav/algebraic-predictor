from functools import wraps

from flask import request

from app.models import User
from app.utils.token import get_token


def admin_only(func):
    """
    make view for users with admin privileges
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = get_token(request)
        if not User().is_admin(token):
            return {'error': 'permission denied'}, 403
        return func(*args, **kwargs)
    return wrapper


def auth_required(func):
    """
    force request to have Authorization header
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = get_token(request)
        if not token:
            return {'error': 'auth required'}, 401
        if not User().get_user(token=token):
            return {'error': 'wrong credentials'}, 400
        kwargs['token'] = token
        return func(*args, **kwargs)
    return wrapper
