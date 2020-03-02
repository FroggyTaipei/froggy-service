import uuid
from django.test import TestCase, tag
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.conf import settings
from rest_framework.exceptions import ValidationError
from apps.cases.models import Case
from apps.users.models import User
from apps.files import models
from .storages import TempStorage

ROOT_DIR = settings.ROOT_DIR


class BaseTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            email='test@test.test',
            password='123456',
            is_staff=True,
            is_superuser=True
        )


@tag('files')
class TempFileTestCase(BaseTestCase):

    def upload(self, file_name, case_uuid):
        file = SimpleUploadedFile(file_name, open(ROOT_DIR('apps/files/test.txt'), 'rb').read())
        return models.TempFile.objects.create(
            user=self.user,
            case_uuid=case_uuid,
            file=file,
        )

    def test_delete(self):
        file = self.upload('test.txt', uuid.uuid4())
        file_name = file.file.name
        self.assertTrue(TempStorage().exists(name=file_name))
        file.delete()
        self.assertFalse(TempStorage().exists(name=file_name))

    def test_duplicate_raise(self):
        file1 = self.upload('test.txt', uuid.uuid4())
        with self.assertRaises(ValidationError):
            self.upload('test.txt', file1.case_uuid)


@tag('files')
class CaseFileTestCase(TempFileTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Load fixtures
        call_command('loaddata', 'region', verbosity=0)
        call_command('loaddata', 'type', verbosity=0)
        call_command('loaddata', 'case.test.yaml', verbosity=0)
        call_command('loaddata', 'sendgrid-template.yaml', verbosity=0)

        cls.case = Case.objects.first()

    def test(self):
        case_uuid = uuid.uuid4()
        temp_file1 = self.upload('test1.txt', case_uuid)
        temp_file2 = self.upload('test2.txt', case_uuid)
        case_copy = {
            **self.case.to_dict(),
            'uuid': case_uuid
        }
        case = Case.objects.create(**case_copy)
        self.assertEqual(case.casefiles.count(), 2)
        self.assertTrue(case.casefiles.filter(file_name=temp_file1.file_name).exists())
        self.assertTrue(case.casefiles.filter(file_name=temp_file2.file_name).exists())
