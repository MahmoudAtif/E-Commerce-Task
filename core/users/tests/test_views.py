from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from core.utils.response_codes import GeneralCodes, UserCodes
from core.users.models import User
from django.contrib.auth import authenticate


class TestView(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='user',
            email='user@gmail.com',
            password='user'
        )

    def test_sign_up_view(self):
        """Test sign-up create view """
        url = reverse('users:sign-up')
        data = {
            "username": "TestUser",
            "email": "TestUser@gmail.com",
            "password": "123456789aaaaaaaa",
            "confirm_password": "123456789aaaaaaaa"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('username'), data['username'])
        self.assertEqual(response.data.get('email'), data['email'])
        self.assertEqual(response.data.get('code'), GeneralCodes.SUCCESS)

    def test_password_not_match_sign_up_view(self):
        """Test password not match sign-up"""
        url = reverse('users:sign-up')
        data = {
            "username": "TestUser",
            "email": "TestUser@gmail.com",
            "password": "12345678a",
            "confirm_password": "123456789aaaaaaaa"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get('code')[0],
            UserCodes.PASSWORD_NOT_MATCH
        )

    def test_username_sign_in_view(self):
        """Test sign-in view with username"""
        url = reverse('users:sign-in')
        data = {
            "username_or_email": "user",
            "password": "user"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('code'), GeneralCodes.SUCCESS)

    def test_email_sign_in_view(self):
        """Test sign-in view with email"""
        url = reverse('users:sign-in')
        data = {
            "username_or_email": "user@gmail.com",
            "password": "user"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('code'), GeneralCodes.SUCCESS)

    def test_sign_in_with_wrong_data(self):
        """Test sign-in view with wrong data"""
        url = reverse('users:sign-in')
        data = {
            "username_or_email": "user555",
            "password": "user"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data.get('code')[0],
            UserCodes.INVALID_CREDENTIALS
        )

    def test_username_authenticate_funcion(self):
        """Test authenticate user with username"""
        user = authenticate(username='user', password='user')
        self.assertEqual(self.user, user)

    def test_email_authenticate_funcion(self):
        """Test authenticate user with email"""
        user = authenticate(username='user@gmail.com', password='user')
        self.assertEqual(user, self.user)

    def test_authenticate_with_wrong_credentials(self):
        """Test authenticate user with username"""
        user = authenticate(username='usedsfdsgdr', password='usedfgfgr')
        self.assertEqual(user, None)
