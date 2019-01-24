import logging
from datetime import datetime, timedelta

from apps.users.utils import jwt_encode_handler
from apps.users.models import User


logger = logging.getLogger('raven')


def create_superuser():
    """Initial fake superuser only for testing. Use in docker-compose."""
    email = 'test@test.test'
    password = '123456'
    mobile = '0912345678'
    if not User.objects.count():
        user = User.objects.create_user(email=email, password=password,
                                        full_name='Test Superuser', mobile=mobile,
                                        is_staff=True, is_superuser=True)
        payload = {
            'id': user.pk,
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


create_superuser()
