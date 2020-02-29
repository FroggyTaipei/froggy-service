import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class BaseFileSystemStorage:
    relative_location = None
    relative_base_url = None

    def __new__(cls):
        location = os.path.join(settings.MEDIA_ROOT, cls.relative_location)
        base_url = os.path.join(settings.MEDIA_URL, cls.relative_base_url)
        if not os.path.exists(location):
            os.makedirs(location)
        return FileSystemStorage(location=location, base_url=base_url)


class CaseStorage(BaseFileSystemStorage):
    relative_location = relative_base_url = 'case-files'


class TempStorage(BaseFileSystemStorage):
    relative_location = relative_base_url = 'temp-files'
