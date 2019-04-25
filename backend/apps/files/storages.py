"""
GoogleCloudStorage extensions suitable for handing Django's
Static and Media files.

Requires following settings:
MEDIA_URL, GS_MEDIA_BUCKET_NAME
STATIC_URL, GS_STATIC_BUCKET_NAME

In addition to
https://django-storages.readthedocs.io/en/latest/backends/gcloud.html
"""
from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import setting
from urllib.parse import urljoin


class GoogleCloudMediaStorage(GoogleCloudStorage):
    """GoogleCloudStorage suitable for Django's Media files."""

    def __init__(self, *args, **kwargs):
        if not settings.MEDIA_URL:
            raise Exception('MEDIA_URL has not been configured')
        kwargs['bucket_name'] = setting('GS_MEDIA_BUCKET_NAME')
        super(GoogleCloudMediaStorage, self).__init__(*args, **kwargs)

    def url(self, name):
        """.url that doesn't call Google."""
        return urljoin(settings.MEDIA_URL, name)


class GoogleCloudStaticStorage(GoogleCloudStorage):
    """GoogleCloudStorage suitable for Django's Static files"""

    def __init__(self, *args, **kwargs):
        if not settings.STATIC_URL:
            raise Exception('STATIC_URL has not been configured')
        kwargs['bucket_name'] = setting('GS_STATIC_BUCKET_NAME')
        super(GoogleCloudStaticStorage, self).__init__(*args, **kwargs)

    def url(self, name):
        """.url that doesn't call Google."""
        return urljoin(settings.STATIC_URL, name)


class CleanStorage(object):
    """
    使用Traversal將Storage清空
    """
    def __init__(self, storage=None, **kwargs):
        self.storage = storage
        self.clean_storage(self.storage)

    def clean_file(self, path, file_list):
        for i in file_list:
            if path[-1:] is '/':
                self.storage.delete(f'{path}{i}')
            else:
                self.storage.delete(f'{path}/{i}')

    def clean_dir(self, path, directory):
        storage_list = self.storage.listdir(f'{path}{directory}/')
        self.clean_file(f'{path}{directory}/', storage_list[1])
        for i in storage_list[0]:
            self.clean_dir(f'{path}{directory}/', i)
        if path[-1:] is '/':
            if self.storage.exists(f'{path}{directory}'):
                self.storage.delete(f'{path}{directory}')
        else:
            if self.storage.exists(f'{path}{directory}/'):
                self.storage.delete(f'{path}{directory}/')

    def clean_storage(self, storage):
        path = ''
        storage_list = storage.listdir(path)
        self.clean_file(path, storage_list[1])
        for i in storage_list[0]:
            self.clean_dir(path, i)
