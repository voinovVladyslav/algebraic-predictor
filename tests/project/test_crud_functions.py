import pytest
from model_bakery.baker import make
from rest_framework import status

from project.models import Project
from core.models import User
from tests.user.fixtures import create_user
from tests.fixtures import (
    api_client, authenticated_client, user_email, user_password
)
from .urls import PROJECTS_URL, get_project_detail_url


def test_create_project_success(db, authenticated_client, user_email):
    title = 'test title'
    source = 'test source'
    algebraic_model = 'test model'
    payload = {
        'title': title,
        'source': source,
        'algebraic_model': algebraic_model
    }
    assert Project.objects.count() == 0
    response = authenticated_client.post(PROJECTS_URL, payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert Project.objects.count() == 1
    project = Project.objects.first()
    assert project.title == title
    assert project.source == source
    assert project.algebraic_model == algebraic_model
    assert project.user.email == user_email


def test_update_full_project_success(db, authenticated_client, user_email):
    title = 'test title'
    source = 'test source'
    algebraic_model = 'test model'
    user = User.objects.get(email=user_email)
    project = Project.objects.create(
        title='test',
        source='test',
        algebraic_model='test',
        user=user,
    )
    payload = {
        'title': title,
        'source': source,
        'algebraic_model': algebraic_model
    }
    response = authenticated_client.put(
        get_project_detail_url(project.id), payload
    )
    assert response.status_code == status.HTTP_200_OK
    project.refresh_from_db()
    assert project.title == title
    assert project.source == source
    assert project.algebraic_model == algebraic_model


def test_update_title_project_success(db, authenticated_client, user_email):
    user = User.objects.get(email=user_email)
    project = Project.objects.create(
        title='test',
        user=user,
    )
    title = 'test title'
    payload = {
        'title': title,
    }
    response = authenticated_client.patch(
        get_project_detail_url(project.id), payload
    )
    assert response.status_code == status.HTTP_200_OK
    project.refresh_from_db()
    assert project.title == title


def test_delete_project_success(db, authenticated_client, user_email):
    user = User.objects.get(email=user_email)
    project = Project.objects.create(
        title='test',
        user=user,
    )
    title = 'test title'
    payload = {
        'title': title,
    }
    assert Project.objects.count() == 1
    response = authenticated_client.delete(
        get_project_detail_url(project.id), payload
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Project.objects.count() == 0
