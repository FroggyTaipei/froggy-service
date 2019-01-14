from django.test import TestCase
from django.core.management import call_command
from apps.mails.models import SendGridMail, SendGridMailTemplate
from apps.cases.models import Case
from python_http_client.exceptions import HTTPError
from django.test import tag


class SendGridTestCase(TestCase):
    def setUp(self):
        """Load fixtures"""
        call_command('loaddata', 'region', verbosity=0)
        call_command('loaddata', 'type', verbosity=0)
        call_command('loaddata', 'case.test.yaml', verbosity=0)
        call_command('loaddata', 'sendgrid-template.test.yaml', verbosity=0)

        self.case = Case.objects.first()

    def test_template_save(self):
        with self.assertRaises(HTTPError):
            SendGridMailTemplate.objects.create(tid='wrong-id', name='Test Template')

    @tag('private')
    def test_send(self):
        instance = self.case
        data = {
            'number': instance.number,
            'username': instance.username,
            'title': instance.title,
            'datetime': instance.create_time,
            'content': instance.content,
            'location': instance.location,
        }
        template = SendGridMailTemplate.objects.filter(name='收件通知').first()

        self.assertIsNotNone(template)

        mail = SendGridMail(case=instance, template=template, to_email=instance.email, data=data)
        mail.save()

        self.assertTrue(mail.success, True)

        mail2 = SendGridMail.objects.create(case=instance, template=template,
                                            to_email=instance.email, data=data)

        self.assertTrue(mail2.success, True)

    @tag('private')
    def test_send_case_confirm(self):
        self.case.confirm()
