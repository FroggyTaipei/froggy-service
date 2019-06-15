from django.test import TransactionTestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from apps.users.models import User


class UserModelTestCase(TransactionTestCase):
    def test_create_normal_user(self):
        user = User.objects.create_user(email='normal@mail.com', password='123456', is_staff=True, is_superuser=True)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_create_accountkit_use(self):
        user = User.objects.create_accountkit_user(mobile='0912345678', email=None)
        self.assertTrue(user.is_active)

        with self.assertRaises(IntegrityError):
            User.objects.create_accountkit_user(mobile='0912345678', email=None)

        user = User.objects.create_accountkit_user(mobile=None, email='test@tester.email.com')
        self.assertTrue(user.is_active)

        with self.assertRaises(IntegrityError):
            User.objects.create_accountkit_user(mobile=None, email='test@tester.email.com')

        with self.assertRaises(ValidationError):
            User.objects.create_accountkit_user(mobile=None, email=None)

        with self.assertRaises(ValidationError):
            User.objects.create_accountkit_user(mobile='0912345679', is_staff=True, is_superuser=True)
