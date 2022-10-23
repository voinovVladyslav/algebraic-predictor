from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from project.models import Project
from project.serializers import ProjectSerializer


PROJECT_URL = reverse('project:project-list')

def project_detail(project_id):
    return reverse('project:project-detail', args=[project_id])

def create_user(email, password, **kwargs):
    data = {
        'first_name':'Petro',
        'last_name':'Poroshenko',
    }
    data.update(**kwargs)
    user = get_user_model().objects.create_user(
        email=email,
        password=password,
        **data,
    )
    return user


def create_project(user, **kwargs):
    data = {
        'source':'base source',
        'algebraic_model':'algebraic model',
    }
    data.update(**kwargs)
    return Project.objects.create(user=user, **data)


class PublicProjectApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_authenticated_only(self):
        res = self.client.get(PROJECT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateProjectApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user('petro@roshen.com', 'zeleboba')
        self.client.force_authenticate(self.user)

    def test_get_project_only_for_current_user(self):
        another_user = create_user('vova95@kvartal.ua', 'slava Ukraini')
        another_project = create_project(another_user, source='roshen')
        project = create_project(self.user, source='different')
        s1 = ProjectSerializer(another_project)
        s2 = ProjectSerializer(project)

        res = self.client.get(PROJECT_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        assert s2.data in res.data
        assert s1.data not in res.data

    def test_successfully_create_project(self):
        data = {
            'source': 'Source',
            'algebraic_model':'Model',
        }

        res = self.client.post(PROJECT_URL, data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertTrue(Project.objects.filter(user=self.user).exists())

    def test_succesfully_update_project(self):
        project = create_project(self.user)
        data = {
            'source':'new',
            'algebraic_model':'new model',
        }
        url = project_detail(project.id)
        res = self.client.put(url, data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        project.refresh_from_db()
        self.assertEqual(project.source, data['source'])
        self.assertEqual(project.algebraic_model, data['algebraic_model'])

    def test_succesfully_delete_project(self):
        project = create_project(self.user)

        url = project_detail(project.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        proj = Project.objects.filter(user=self.user)
        self.assertFalse(proj.exists())
