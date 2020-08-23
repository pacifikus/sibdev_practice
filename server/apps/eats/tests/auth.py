from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.eats.tests import utils


class AuthAPITests(APITestCase):
    def setUp(self):
        self.user_data = {
            "username": "test_user",
            "password": "pass_test",
            "email": "test@test.ru",
        }
        self.user_data_new = {
            "username": "qwe123123",
            "password": "qwe1",
        }
        self.token, self.user = utils.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password'],
        )

    def test_users_create_action_returns_token(self):
        """
        Test: User POST returns authtoken
        """
        url = reverse('users-list')
        response = self.client.post(url, self.user_data_new, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('token' in response.data)
        self.assertNotEqual(response.data['token'], '')

    def test_auth_token_returns_token(self):
        """
        Test: auth/token/ POST returns authtoken
        """
        response = self.client.post('/api/auth/token/', self.user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        self.assertNotEqual(response.data['token'], '')
