from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagersTests(TestCase):

    def setUp(self):
        # Clear all users before each test
        User = get_user_model()
        User.objects.all().delete()

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="user@email.com", password="testpass123")
        self.assertEqual(user.email, "user@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="testpass123")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email="admin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.email, "admin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="admin@email.com", password="testpass123", is_superuser=False
            )
