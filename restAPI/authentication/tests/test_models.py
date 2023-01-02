from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            'akolade', 'emmakolade@gmail.com', 'Password123##')  # checks if users can be created
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'emmakolade@gmail.com')

    def test_create_super_user(self):
        user = User.objects.create_superuser(
            'akolade', 'emmakolade@gmail.com', 'Password123##')  # checks if users can be created
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'emmakolade@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='',
                          email='emmakolade@gmail.com', password='Password123##')
        self.assertRaisesMessage(ValueError, "The given username must be set")

    def test_raises_error_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, "The given username must be set"):
            User.objects.create_user(
                username='', email='emmakolade@gmail.com', password='Password123##')

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username='akolade', email='', password='Password123##')
        self.assertRaisesMessage(ValueError, "The given email must be set")

    def test_raises_error_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, "The given email must be set"):
            User.objects.create_user(
                username='akolade', email='', password='Password123##')

    def test_cant_create_super_user_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_staff=True."):
            User.objects.create_superuser(
                username='akolade', email='emmakolade@gmail.com', password='Password123##', is_staff=False)

    def test_cant_create_super_user_with_no_super_user_status(self):
        with self.assertRaisesMessage(ValueError, "Superuser must have is_superuser=True."):
            User.objects.create_superuser(
                username='akolade', email='emmakolade@gmail.com', password='Password123##', is_superuser=False)
