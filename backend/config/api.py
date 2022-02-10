from rest_framework import routers
from apps.users.views import UserViewSet
from apps.mails.views import MailViewSet
from apps.files.views import TempFileViewSet
from apps.cases.views import (
    TypeViewSet,
    RegionViewSet,
    CaseViewSet,
    CaseInsightViewSet,
)
from apps.marquees.views import MarqueeMessageViewSet


# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet, basename='users')

# Mails API
api.register(r'mails', MailViewSet)

# Files API
api.register(r'files/temp', TempFileViewSet)

# Cases API
api.register(r'cases', CaseViewSet)
api.register(r'cases/insights', CaseInsightViewSet, basename='cases-insights')
api.register(r'types', TypeViewSet)
api.register(r'regions', RegionViewSet)

# Marquees API
api.register(r'marquees', MarqueeMessageViewSet)
