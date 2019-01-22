import datetime
import os
import uuid

from storages.backends.gcloud import GoogleCloudStorage
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from rest_framework.exceptions import ValidationError
from apps.cases.models import Case
from apps.users.models import User
from apps.files import models

from .storages import CleanStorage


ROOT_DIR = settings.ROOT_DIR


"""Set Up Storage"""
if settings.USE_GCS:
    TEMP_BUCKET = f'{settings.GS_BUCKET_NAME}-test-temp'
    CASE_BUCKET = f'{settings.GS_BUCKET_NAME}-test-case'
    TEMP_STORAGE = GoogleCloudStorage(bucket_name=TEMP_BUCKET)
    CASE_STORAGE = GoogleCloudStorage(bucket_name=CASE_BUCKET)
else:
    temp_dir = f'{settings.MEDIA_ROOT}/test-temp/'
    case_dir = f'{settings.MEDIA_ROOT}/test-casefile/'
    TEMP_STORAGE = FileSystemStorage(location=temp_dir, base_url=temp_dir)
    CASE_STORAGE = FileSystemStorage(location=case_dir, base_url=case_dir)
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    if not os.path.exists(case_dir):
        os.mkdir(case_dir)


class CleanStorageTestCase(TestCase):
    def setUp(self):
        """Create User"""
        user = User.objects.create_user(email='normal@mail.com', password='123456', is_staff=True, is_superuser=True)

        """Clean Storage by Traversal"""
        CleanStorage(storage=TEMP_STORAGE)
        CleanStorage(storage=CASE_STORAGE)

        """Set Up Default File"""
        """Upload File to Temp Storage"""
        file = SimpleUploadedFile('test.txt', open(ROOT_DIR('apps/files/test.txt'), 'rb').read())
        temp = models.TempFile()
        temp.user = user
        temp.case_uuid = uuid.uuid4()
        temp.file = file
        temp.file.storage = TEMP_STORAGE
        temp.save()

        """Upload File to Case Storage"""
        file2 = SimpleUploadedFile('test.txt', open(ROOT_DIR('apps/files/test.txt'), 'rb').read())
        temp2 = models.TempFile()
        temp2.user = user
        temp2.case_uuid = uuid.uuid4()
        temp2.file = file2
        temp2.file.storage = CASE_STORAGE
        temp2.save()

    def test_clean_storage(self):
        self.assertEqual(len(TEMP_STORAGE.listdir('')[0]), 1)
        self.assertEqual(len(TEMP_STORAGE.listdir('')[1]), 0)
        self.assertEqual(len(CASE_STORAGE.listdir('')[0]), 1)
        self.assertEqual(len(CASE_STORAGE.listdir('')[1]), 0)

        """Clean Storage by Traversal"""
        CleanStorage(storage=TEMP_STORAGE)
        CleanStorage(storage=CASE_STORAGE)

        self.assertEqual(len(TEMP_STORAGE.listdir('')[0]), 0)
        self.assertEqual(len(TEMP_STORAGE.listdir('')[1]), 0)
        self.assertEqual(len(CASE_STORAGE.listdir('')[0]), 0)
        self.assertEqual(len(CASE_STORAGE.listdir('')[1]), 0)


class TempFileCRUDTestCase(TestCase):
    """
    測試TempFile CRUD 功能
    """
    def setUp(self):
        """Create User"""
        user = User.objects.create_user(email='normal@mail.com', password='123456', is_staff=True, is_superuser=True)

        """Clean Storage by Traversal"""
        CleanStorage(storage=TEMP_STORAGE)
        CleanStorage(storage=CASE_STORAGE)

        """Set Up Default File"""
        """Upload File to Temp Storage"""
        file = SimpleUploadedFile('test.txt', open(ROOT_DIR('apps/files/test.txt'), 'rb').read())
        temp = models.TempFile()
        temp.user = user
        temp.case_uuid = uuid.uuid4()
        temp.file = file
        temp.file.storage = TEMP_STORAGE
        temp.save()

        self.obj = models.TempFile.objects.first()
        self.obj.file.storage = TEMP_STORAGE
        self.objs = models.TempFile.objects.all()

    def test_save(self):
        self.assertEqual(self.objs.count(), 1)
        self.assertEqual(TEMP_STORAGE.exists(name=self.obj.file.name), True)

    def test_delete(self):
        self.obj.delete()
        self.assertEqual(self.objs.count(), 0)
        self.assertEqual(TEMP_STORAGE.exists(name=self.obj.file.name), False)


class TempFileTestCase(TestCase):
    """
    測試TempFile相關功能
    """
    def setUp(self):
        """Create User"""
        self.user = User.objects.create_user(email='normal@mail.com', password='123456', is_staff=True, is_superuser=True)
        self.uuid = uuid.uuid4()

        """Clean Storage by Traversal"""
        CleanStorage(storage=TEMP_STORAGE)
        CleanStorage(storage=CASE_STORAGE)

        """Set Up Default File"""
        """Upload File to Temp Storage"""
        file = SimpleUploadedFile('test.txt', open(ROOT_DIR('apps/files/test.txt'), 'rb').read())
        temp = models.TempFile()
        temp.user = self.user
        temp.case_uuid = self.uuid
        temp.file = file
        temp.file.storage = TEMP_STORAGE
        temp.save()

        self.obj = models.TempFile.objects.first()
        self.obj.file.storage = TEMP_STORAGE
        self.objs = models.TempFile.objects.all()

    def test_duplicate(self):
        """
        當某個案件上傳重複檔名的檔案時，預期會出現錯誤
        """
        file2 = SimpleUploadedFile('test.txt', open(ROOT_DIR('apps/files/test.txt'), 'rb').read())
        temp2 = models.TempFile()
        temp2.user = self.user
        temp2.case_uuid = self.uuid
        temp2.file = file2
        temp2.file.storage = TEMP_STORAGE

        with self.assertRaises(ValidationError):
            temp2.save()


class TempFileExpireTestCase(TestCase):
    """
    測試TempFile移除超過時間未送出案件的檔案
    """
    def setUp(self):
        """Create User"""
        user = User.objects.create_user(email='normal@mail.com', password='123456', is_staff=True, is_superuser=True)

        """Clean Storage by Traversal"""
        CleanStorage(storage=TEMP_STORAGE)
        CleanStorage(storage=CASE_STORAGE)

        """Set Up Default File"""
        """Upload File to Temp Storage"""
        file = SimpleUploadedFile('test.txt', open(ROOT_DIR('apps/files/test.txt'), 'rb').read())
        temp = models.TempFile()
        temp.user = user
        temp.case_uuid = uuid.uuid4()
        temp.file = file
        temp.file.storage = TEMP_STORAGE
        temp.save()

        self.obj = models.TempFile.objects.first()
        self.obj.file.storage = TEMP_STORAGE
        self.objs = models.TempFile.objects.all()

    def test_unexpired(self):
        today = datetime.date.today()
        expire_list = self.objs.filter(upload_time__date__lt=today)
        for i in expire_list:
            i.file.storage = TEMP_STORAGE
            i.delete()
        self.assertEqual(self.objs.count(), 1)

    def test_expired(self):
        day_after_tomorrow = datetime.date.today() + datetime.timedelta(2)
        expire_list = self.objs.filter(upload_time__date__lt=day_after_tomorrow)
        for i in expire_list:
            i.file.storage = TEMP_STORAGE
            i.delete()
        self.assertEqual(self.objs.count(), 0)


class CaseFileTestCase(TestCase):
    """
    測試CaseFile相關功能
    """
    def setUp(self):
        """Create User"""
        user = User.objects.create_user(email='normal@mail.com', password='123456', is_staff=True, is_superuser=True)

        """Clean Storage by Traversal"""
        CleanStorage(storage=TEMP_STORAGE)
        CleanStorage(storage=CASE_STORAGE)

        """Load fixtures"""
        call_command('loaddata', 'region', verbosity=0)
        call_command('loaddata', 'type', verbosity=0)
        call_command('loaddata', 'case.test.yaml', verbosity=0)
        self.case = Case.objects.first()

        """Set Up Default File"""
        """Upload File to Temp Storage"""
        file = SimpleUploadedFile('test1.txt', open(ROOT_DIR('apps/files/test.txt'), 'rb').read())
        temp = models.TempFile()
        temp.user = user
        temp.case_uuid = self.case.uuid
        temp.file = file
        temp.file.storage = TEMP_STORAGE
        temp.save()

        file2 = SimpleUploadedFile('test2.txt', open(ROOT_DIR('apps/files/test.txt'), 'rb').read())
        temp2 = models.TempFile()
        temp2.user = user
        temp2.case_uuid = self.case.uuid
        temp2.file = file2
        temp2.file.storage = TEMP_STORAGE
        temp2.save()

        self.objs = models.TempFile.objects.filter(case_uuid=self.case.uuid)

    def test_case_create_copy_file(self):
        """
        案件成立時，將檔案從暫存bucket複製到案件bucket
        並將每個檔案關聯到案件，暫存bucket的檔案不會被刪除
        """
        for i in self.objs:
            file = TEMP_STORAGE._open(i.file.name)
            case_file = models.CaseFile()
            case_file.case = self.case
            case_file.file = file
            case_file.file.storage = CASE_STORAGE
            case_file.save()

        case1 = models.CaseFile.objects.first()
        case2 = models.CaseFile.objects.last()
        self.assertEqual(models.CaseFile.objects.all().count(), 2)
        self.assertEqual(CASE_STORAGE.exists(case1.file.name), True)
        self.assertEqual(CASE_STORAGE.exists(case2.file.name), True)
