from django.test import TestCase, tag
from django.utils import timezone
from django.core.management import call_command
from django.core.exceptions import ValidationError

from django_fsm import TransitionNotAllowed

from apps.cases.models import Case, CaseHistory
from apps.arranges.models import Arrange


class CaseModelTestCase(TestCase):
    def setUp(self):
        """Load fixtures"""
        call_command('loaddata', 'region', verbosity=0)
        call_command('loaddata', 'type', verbosity=0)
        call_command('loaddata', 'case.test.yaml', verbosity=0)
        call_command('loaddata', 'sendgrid-template.yaml', verbosity=0)

        self.case = Case.objects.first()
        self.case_history = CaseHistory.objects.first()

    def test_manager_update(self):
        Case.objects.create(**self.case.to_dict())
        Case.objects.create(**self.case.to_dict())

        self.assertEqual(Case.objects.count(), 3)
        new_title = '\u53F0\u5317\u5E02\u677E\u5C71\u5340\u5FA9\u8208\u5317\u8DEF'
        new_username = 'John Doe'
        Case.objects.all().update(title=new_title, username=new_username)

        self.assertEqual(Case.objects.filter(title=new_title).count(), 3)
        self.assertEqual(Case.objects.filter(username=new_username).count(), 3)


class CaseCrudTestCase(TestCase):
    def setUp(self):
        """Load fixtures"""
        call_command('loaddata', 'region', verbosity=0)
        call_command('loaddata', 'type', verbosity=0)
        call_command('loaddata', 'case.test.yaml', verbosity=0)
        call_command('loaddata', 'sendgrid-template.yaml', verbosity=0)

        self.case = Case.objects.filter(state='draft').first()
        self.case_history = CaseHistory.objects.first()

    def test_set_up(self):
        self.assertTrue(Case.objects.count() > 0)
        self.assertTrue(CaseHistory.objects.count() > 0)

    def test_transition(self):
        qs = CaseHistory.objects.filter(case=self.case)

        self.case.save()
        self.assertEqual(qs.count(), 1)

        with self.assertRaises(TransitionNotAllowed):
            self.case.arrange()

        self.case.username = 'John Doe'
        self.case.save()
        self.assertEqual(qs.count(), 2)
        self.case.arrange()
        self.case.save()
        self.assertIsNotNone(self.case.open_time)
        self.assertEqual(qs.count(), 3)

        with self.assertRaises(TransitionNotAllowed):
            self.case.close()

        arrange = Arrange.objects.create(case=self.case, title='1', content='1', order=1)

        with self.assertRaises(TransitionNotAllowed):
            self.case.close()

        with self.assertRaises(TransitionNotAllowed):
            arrange.publish()

        arrange.arrange_time = timezone.now()
        arrange.publish()
        arrange.save()

        self.case.close()
        self.case.save()
        self.assertIsNotNone(self.case.close_time)
        self.assertEqual(qs.count(), 4)
        self.case.save()
        self.assertEqual(qs.count(), 4)

    def test_case_update(self):
        # Update via instance
        title = self.case.title
        self.case.title = 'new title'
        self.case.save()
        qs = CaseHistory.objects.filter(case=self.case)
        self.assertEqual(qs.count(), 2)

        # Update via Queryset
        Case.objects.filter(id=self.case.id).update(title='new title 2')
        qs = CaseHistory.objects.filter(case=self.case)
        self.assertEqual(qs.count(), 3)

        self.assertEqual(self.case.first_history.title, title)

    def test_case_delete(self):
        self.case.delete()
        qs = CaseHistory.objects.filter(case=self.case)
        self.assertEqual(qs.count(), 0)
