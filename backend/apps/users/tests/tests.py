from django.test import TransactionTestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from apps.users.models import User

from .initial import create_superuser


class UserModelTestCase(TransactionTestCase):
    def test_create_superuser_by_script(self):
        """Load superuser"""
        create_superuser()
        self.superuser = User.objects.first()
        self.assertIsNotNone(self.superuser)

    def test_create_normal_user(self):
        user = User.objects.create_user(email='normal@mail.com', password='123456', is_staff=True, is_superuser=True)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_active)

    def test_create_accountkit_use(self):
        user = User.objects.create_accountkit_user(mobile='+886972505939', email=None)
        self.assertTrue(user.is_active)

        with self.assertRaises(IntegrityError):
            User.objects.create_accountkit_user(mobile='+886972505939', email=None)

        user = User.objects.create_accountkit_user(mobile=None, email='test@tester.email.com')
        self.assertTrue(user.is_active)

        with self.assertRaises(IntegrityError):
            User.objects.create_accountkit_user(mobile=None, email='test@tester.email.com')

        with self.assertRaises(ValidationError):
            User.objects.create_accountkit_user(mobile=None, email=None)

        with self.assertRaises(ValidationError):
            user = User.objects.create_accountkit_user(mobile='+886972505937', is_staff=True, is_superuser=True)

    def test_create_token(self):
        user = User.objects.create_accountkit_user(mobile='+886972505939', email=None)
        token = Token.objects.create(user=user)

        self.assertEqual(token, Token.objects.get(user=user))

        Token.objects.filter(user=user).delete()


