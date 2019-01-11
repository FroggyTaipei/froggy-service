from rest_framework.authtoken.models import Token
from apps.users.models import User


def create_superuser():
    """Initial fake superuser only for testing. Use in docker-compose."""
    email = 'test@mail.com'
    password = '123456'
    token = '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
    if not User.objects.count():
        user = User.objects.create_user(email=email, password=password, full_name='測試用超級使用者',
                                        is_staff=True, is_superuser=True)
        token = Token(key=token, user=user)
        token.save()


create_superuser()
