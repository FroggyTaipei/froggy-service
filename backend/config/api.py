from rest_framework import routers
from apps.users.views import UserViewSet
from apps.mails.views import MailViewSet
from apps.files.api.views import TempFileViewSet, CaseFileViewSet


# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)

# Mails API
api.register(r'mails', MailViewSet)

# Files API
api.register(r'files/temp', TempFileViewSet)
api.register(r'files/case', CaseFileViewSet)
