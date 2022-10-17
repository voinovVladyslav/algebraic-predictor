from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient


USER_CREATE_URL = reverse("user:create")
TOKEN_URL = reverse("user:token")


def create_user(email='test@example.com', password='testpassword', **kwargs):
    data = {
        "fist_name": "Petro",
        "last_name": "Poroshenko",
    }
    data.update(**kwargs)
    return get_user_model().objects.create_user(
        email=email,
        password=password,
        **kwargs
    )


class CreateUserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user_with_only_necessary_fields_success(self):
        data = {
            "email": "test@example.com",
            "password": "testpassword123",
        }

        response = self.client.post(USER_CREATE_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = str(response.content)
        self.assertIn(data["email"], response_data)
        self.assertNotIn(data["password"], response_data)
        user = get_user_model().objects.filter(email=data["email"])
        self.assertTrue(user.exists())

    def test_create_user_with_all_fields_succeess(self):
        data = {
            "email": "test@example.com",
            "password": "testpassword",
            "first_name": "First",
            "last_name": "Last",
        }

        response = self.client.post(USER_CREATE_URL, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = str(response.content)
        self.assertIn(data["email"], response_data)
        self.assertIn(data["first_name"], response_data)
        self.assertIn(data["last_name"], response_data)
        self.assertNotIn(data["password"], response_data)

        user = get_user_model().objects.filter(email=data["email"])
        self.assertTrue(user.exists())

    def test_create_user_invalid_credentials(self):
        data = {
            "email": "test",
            "password": "testpassword",
        }

        response = self.client.post(USER_CREATE_URL, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        user = get_user_model().objects.filter(email=data["email"])
        self.assertFalse(user.exists())

    def test_create_user_password_too_short(self):
        data = {
            "email": "test@example.com",
            "password": "short",
        }

        response = self.client.post(USER_CREATE_URL, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        user = get_user_model().objects.filter(email=data["email"])
        self.assertFalse(user.exists())

    def test_create_user_with_alrealy_taken_email(self):
        user = create_user(email="test@example.com")

        data = {
            "email": "test@example.com",
            "password": "testpassword",
        }

        response = self.client.post(USER_CREATE_URL, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TokenAuthenticationApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_successful_authentication(self):
        data = {
            "email": "dima@example.com",
            "password": "strongpassword",
        }
        user = create_user(**data)

        res = self.client.post(TOKEN_URL, data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('token', res.data)

    def test_wrong_credentials(self):
        data = {
            "email": "dima@example.com",
            "password": "strongpassword",
        }
        user = create_user(email='test@example.com', password='testpassword')

        res = self.client.post(TOKEN_URL, data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)
