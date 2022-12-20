import hashlib

from uuid import uuid4

from app import config


def secure_password(password: str) -> str:
    password_to_secure = password + config['development'].SECRET_KEY
    hashed_pass = hashlib.sha256(password_to_secure.encode()).hexdigest()
    return hashed_pass


def generate_token() -> str:
    return uuid4().hex
