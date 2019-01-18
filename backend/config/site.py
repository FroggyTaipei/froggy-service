from django.contrib.admin.sites import AdminSite
from django.urls import path

from .views import DashboardMainView


class DashboardSite(AdminSite):
    """A Django AdminSite to allow registering custom dashboard views."""

    def get_urls(self):
        urls = super(DashboardSite, self).get_urls()
        custom_urls = [
            path('', self.admin_view(DashboardMainView.as_view()), name='index'),
        ]
        del urls[0]
        return custom_urls + urls
