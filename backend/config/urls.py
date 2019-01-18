from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin
from django.conf.urls import include

from rest_framework_swagger.views import get_swagger_view

from config.api import api

from .views import get_token
from .site import DashboardSite

admin.site = DashboardSite()
admin.sites.site = admin.site
admin.autodiscover()

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include(api.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/docs/', schema_view),
    path('api/csrftoken/', get_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
