from apps.users.models import User


def create_superuser():
    """Initial fake superuser only for testing. Use in docker-compose."""
    email = 'test@mail.com'
    password = '123456'
    if not User.objects.count():
        User.objects.create_user(email=email, password=password, full_name='測試用超級使用者',
                                 is_staff=True, is_superuser=True)


create_superuser()
