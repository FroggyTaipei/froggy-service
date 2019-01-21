from python_http_client.exceptions import HTTPError
from django.test import TestCase, tag
from django.conf import settings
from django.core.management import call_command
from apps.mails.models import SendGridMail, SendGridMailTemplate
from apps.cases.models import Case


class SendGridTestCase(TestCase):
    def setUp(self):
        """Load fixtures"""
        call_command('loaddata', 'region', verbosity=0)
        call_command('loaddata', 'type', verbosity=0)
        call_command('loaddata', 'case.test.yaml', verbosity=0)
        call_command('loaddata', 'sendgrid-template.yaml', verbosity=0)

        self.case = Case.objects.first()

    def test_template_save(self):
        if settings.USE_SENDGRID:
            with self.assertRaises(HTTPError):
                SendGridMailTemplate.objects.create(tid='wrong-id', name='Test Template')

    @tag('mail')
    def test_template(self):
        if settings.USE_SENDGRID:
            for template in SendGridMailTemplate.objects.all():
                response = template.retrieve_template()
                self.assertEqual(response.status_code, 200)

    @tag('mail')
    def test_send(self):
        if settings.USE_SENDGRID:
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

            mail = SendGridMail(case=instance, template=template, to_email='travishen.tw@gmail.com', data=data)
            mail.save()

            self.assertTrue(mail.success, True)

            mail2 = SendGridMail.objects.create(case=instance, template=template,
                                                to_email='travishen.tw@gmail.com', data=data)

            self.assertTrue(mail2.success, True)
