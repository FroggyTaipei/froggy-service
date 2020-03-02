from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config.api import api

from .site import DashboardSite

admin.site = DashboardSite()
admin.sites.site = admin.site
admin.autodiscover()

schema_view = get_schema_view(
    openapi.Info(
        title="Froggy's Service API",
        default_version='v1',
        contact=openapi.Contact(email=settings.SERVER_EMAIL),
        license=openapi.License(name="MIT License"),
    ),
    url=settings.DOMAIN,
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # All Kubernetes services must serve a 200 page at '/', set admin page as index
    path('', admin.site.urls, name='admin'),
    path('api/', include(api.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns[0] = path('admin/', admin.site.urls, name='admin')
