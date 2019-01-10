from rest_framework import routers
from apps.users.views import UserViewSet
from apps.mails.views import MailViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)
# Mails API
api.register(r'mails', MailViewSet)
