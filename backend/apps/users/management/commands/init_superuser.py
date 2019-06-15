import logging
from datetime import datetime
from django.core.management.base import BaseCommand

from apps.users.utils import jwt_encode_handler
from apps.users.models import User


logger = logging.getLogger('raven')


class Command(BaseCommand):
    help = 'Create an superuser with JWT token for testing.'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('password', type=str, help='User password')

    def handle(self, *args, **kwargs):
        email = kwargs['email']
        password = kwargs['password']

        if not User.objects.filter(email=email).first():
            superuser = User.objects.create_superuser(email=email, password=password,
                                                      full_name='Test Superuser')
            payload = {
                'id': superuser.pk,
                'exp': datetime(year=2030, month=1, day=1),
            }
            token = jwt_encode_handler(payload)
            logger.info(f"""

Your initial superuser has been set for testing, use this user to sign in Django admin:

    Email: {email}
    Password: {password}

Use this token for jwt testing, expired in 2030/01/01:

    Authorization: JWT {token}

""")
