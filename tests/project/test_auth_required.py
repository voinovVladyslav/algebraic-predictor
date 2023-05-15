import pytest

from tests.user.fixtures import create_user
from tests.fixtures import api_client, authenticated_client
from .urls import PROJECTS_URL, get_project_detail_url


@pytest.mark.parametrize(
    'method_name,status_code',
    [
        ('get', 401),
        ('post', 401),
    ],
    ids=[
        'auth required for GET',
        'auth required for POST',
    ]
)
def test_auth_required_for_project_list(
    db, api_client, method_name, status_code
):
    response = getattr(api_client, method_name)(PROJECTS_URL)
    assert response.status_code == status_code


@pytest.mark.parametrize(
    'method_name,status_code',
    [
        ('get', 401),
        ('post', 401),
        ('put', 401),
        ('patch', 401),
        ('delete', 401),
    ],
    ids=[
        'auth required for GET',
        'auth required for POST',
        'auth required for PUT',
        'auth required for PATCH',
        'auth required for DELETE',
    ]
)
def test_auth_required_for_project_detail(
    db, api_client, method_name, status_code
):
    response = getattr(api_client, method_name)(get_project_detail_url(1))
    assert response.status_code == status_code
