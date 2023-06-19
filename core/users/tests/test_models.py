from rest_framework.test import APITestCase
from core.users.models import User


class TestModel(APITestCase):

    def test_create_user(self):
        user = User.objects.create(
            username='Test',
            email='Test@gmail.com',
            password='Test'
        )
        self.assertEqual(user.username, 'Test')
        self.assertEqual(user.email, 'Test@gmail.com')
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)

    def test_create_user_manager(self):
        user = User.objects.create_user(
            username='Test2',
            email='Test2@gmail.com',
            password='Test2'
        )
        self.assertEqual(user.username, 'Test2')
        self.assertEqual(user.email, 'Test2@gmail.com')
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)

    def test_create_superuser_manager(self):
        user = User.objects.create_superuser(
            username='Test3',
            email='Test3@gmail.com',
            password='Test3'
        )
        self.assertEqual(user.username, 'Test3')
        self.assertEqual(user.email, 'Test3@gmail.com')
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)
