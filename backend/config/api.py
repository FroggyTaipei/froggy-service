from rest_framework import routers
from apps.users.views import UserViewSet
<<<<<<< HEAD
from apps.mails.views import MailViewSet
=======
from apps.files.api.views import TempFileViewSet, CaseFileViewSet
>>>>>>> temp commit

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)
<<<<<<< HEAD
# Mails API
api.register(r'mails', MailViewSet)
=======

# Filed API
api.register(r'files/temp', TempFileViewSet)
api.register(r'files/case', CaseFileViewSet)
>>>>>>> temp commit
