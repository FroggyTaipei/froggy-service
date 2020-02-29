"""
GoogleCloudStorage extensions suitable for handing Django's
Static and Media files.
In addition to
https://django-storages.readthedocs.io/en/latest/backends/gcloud.html
"""
from django.conf import settings
from google.oauth2 import service_account
from storages.backends.gcloud import GoogleCloudStorage
from urllib.parse import urljoin


class MediaStorage(GoogleCloudStorage):
    """GoogleCloudStorage suitable for Django's Media files."""
    project_id = settings.GS_PROJECT_ID
    credentials = service_account.Credentials.from_service_account_file(settings.DEFAULT_SA_PATH)
    bucket_name = settings.GS_MEDIA_BUCKET
    auto_create_bucket = True

    def __init__(self, *args, **kwargs):
        if not settings.MEDIA_URL:
            raise Exception('MEDIA_URL has not been configured')
        super().__init__(*args, **kwargs)

    def url(self, name):
        """.url that doesn't call Google."""
        return urljoin(settings.MEDIA_URL, name)


class StaticFileStorage(GoogleCloudStorage):
    """GoogleCloudStorage suitable for Django's Static files"""
    credentials = service_account.Credentials.from_service_account_file(settings.DEFAULT_SA_PATH)
    bucket_name = settings.GS_STATIC_BUCKET
    default_acl = 'publicRead'
    auto_create_bucket = True

    def __init__(self, *args, **kwargs):
        if not settings.STATIC_URL:
            raise Exception('STATIC_URL has not been configured')
        super().__init__(*args, **kwargs)

    def url(self, name):
        """.url that doesn't call Google."""
        return urljoin(settings.STATIC_URL, name)
