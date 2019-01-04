from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin

from django.conf.urls import include

from config.api import api

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('mail/', include('apps.mails.urls', namespace='mails')),
    path('api/', include(api.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
