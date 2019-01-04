from django.test import TestCase
from django.core.management import call_command
from apps.cases.models import Status, Case, CaseHistory


class CaseModelTestCase(TestCase):
    def setUp(self):
        """Load fixtures"""
        call_command('loaddata', 'region', verbosity=0)
        call_command('loaddata', 'status', verbosity=0)
        call_command('loaddata', 'type', verbosity=0)
        call_command('loaddata', 'case.test.yaml', verbosity=0)

        self.case = Case.objects.first()
        self.case_history = CaseHistory.objects.first()

    def test_manager_update(self):
        Case.objects.create(**self.case.to_dict())
        Case.objects.create(**self.case.to_dict())

        self.assertEqual(Case.objects.count(), 3)
        new_number = '3kD2af'
        new_username = 'John Doe'
        Case.objects.all().update(number=new_number, username=new_username)

        self.assertEqual(Case.objects.filter(number=new_number).count(), 3)
        self.assertEqual(Case.objects.filter(username=new_username).count(), 3)


class CaseCrudTestCase(TestCase):
    def setUp(self):
        """Load fixtures"""
        call_command('loaddata', 'region', verbosity=0)
        call_command('loaddata', 'status', verbosity=0)
        call_command('loaddata', 'type', verbosity=0)
        call_command('loaddata', 'case.test.yaml', verbosity=0)

        self.case = Case.objects.first()
        self.case_history = CaseHistory.objects.first()

    def test_set_up(self):
        self.assertEqual(Case.objects.count(), 1)
        self.assertEqual(CaseHistory.objects.count(), 1)

    def test_case_create(self):
        case = Case.objects.create(**self.case.to_dict())
        qs = CaseHistory.objects.filter(case=case)
        self.assertEqual(qs.count(), 1)

    def test_case_update(self):
        # Update via instance
        number = self.case.number
        self.case.number = '12Jj4d'
        self.case.save()
        qs = CaseHistory.objects.filter(case=self.case)
        self.assertEqual(qs.count(), 2)

        # Update via Queryset
        Case.objects.filter(id=self.case.id).update(number='3kvJ3C')
        qs = CaseHistory.objects.filter(case=self.case)
        self.assertEqual(qs.count(), 3)

        self.assertEqual(self.case.first_history.number, number)

    def test_case_delete(self):
        self.case.delete()
        qs = CaseHistory.objects.filter(case=self.case)
        self.assertEqual(qs.count(), 0)

    def test_status_change(self):
        self.assertIsNone(self.case.open_time)
        self.assertIsNone(self.case.close_time)

        # Change status
        self.case.status = Status.objects.get(name='已排程')
        self.case.save()

        first_open_time = self.case.open_time
        self.assertIsNotNone(first_open_time)
        self.assertIsNone(self.case.close_time)

        self.case.status = Status.objects.get(name='已結案')
        self.case.save()

        first_close_time = self.case.close_time
        self.assertIsNotNone(first_open_time)
        self.assertIsNotNone(first_close_time)

        # Switch status back
        self.case.status = Status.objects.get(name='處理中')
        self.case.save()
        self.assertIsNotNone(first_open_time)
        self.assertIsNotNone(first_close_time)

        self.case.status = Status.objects.get(name='已結案')
        self.case.save()
        self.assertLess(first_close_time, self.case.close_time)
