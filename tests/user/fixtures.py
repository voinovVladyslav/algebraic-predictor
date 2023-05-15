import pytest
import uuid


@pytest.fixture
def user_email():
    return 'user@example.com'


@pytest.fixture
def user_password():
    return 'testpassword'


@pytest.fixture
def create_user(db, django_user_model, user_email, user_password):
    def make_user(**kwargs):
        kwargs['password'] = user_password
        if 'email' not in kwargs:
            kwargs['email'] = user_email
            return django_user_model.objects.create_user(**kwargs)
    return make_user
