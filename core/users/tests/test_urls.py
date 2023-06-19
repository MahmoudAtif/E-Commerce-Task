from rest_framework.test import APITestCase
from django.urls import resolve, reverse
from core.users import views


class TestUrl(APITestCase):

    def test_sign_up_url(self):
        url = reverse('users:sign-up')
        view = resolve(url).func.cls
        self.assertEqual(view, views.SignUpView)

    def test_sign_in_url(self):
        url = reverse('users:sign-in')
        view = resolve(url).func.cls
        self.assertEqual(view, views.SignInView)