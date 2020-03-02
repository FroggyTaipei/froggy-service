import json
import logging
import sendgrid
from python_http_client.exceptions import HTTPError
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.translation import ugettext_lazy as _
from sendgrid.helpers.mail import Email, Mail
from django.contrib.postgres.fields import HStoreField
from django.db.models import (
    Model,
    CASCADE,
    DateTimeField,
    ForeignKey,
    EmailField,
    BooleanField,
    CharField,
)

logger = logging.getLogger(__name__)


class SendGridMailTemplate(Model):
    """SendGrid樣板"""
    tid = CharField(max_length=255, verbose_name=_('Template Id'))
    name = CharField(max_length=50, verbose_name=_('Name'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    class Meta:
        verbose_name = _('SendGrid Template')
        verbose_name_plural = _('SendGrid Template')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.retrieve_template()  # Test template exist
        super(SendGridMailTemplate, self).save(*args, **kwargs)

    def retrieve_template(self):
        sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
        return sg.client.templates._(self.tid).get()


class SendGridMail(Model):
    """用SendGrid寄出的信件紀錄
    * case: 案件
    * template: 信件樣板
    * from_email: 寄送者
    * to_email: 收件者
    * data: SendGrid Transactional Templates所使用的json資料，使用Postgres的HStoreField儲存，
            詳見https://docs.djangoproject.com/en/2.1/ref/contrib/postgres/fields/#hstorefield
    * success: API請求狀態，若status_code回傳202則紀錄為成功
    * send_time: 發送時間
    """
    case = ForeignKey('cases.Case', on_delete=CASCADE, related_name='sendgrid_mails', verbose_name=_('Case'))
    template = ForeignKey('mails.SendGridMailTemplate', on_delete=CASCADE,
                          related_name='mails', verbose_name=_('SendGrid Template'))
    from_email = EmailField(verbose_name=_('From Email'))
    to_email = EmailField(verbose_name=_('To Email'))
    data = HStoreField(verbose_name=_('Mail Data'))
    success = BooleanField(default=False, verbose_name=_('Request Success'))
    send_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Send Time'))

    class Meta:
        verbose_name = _('SendGrid Mail')
        verbose_name_plural = _('SendGrid Mails')
        ordering = ('-send_time',)

    def __str__(self):
        return self.to_email

    def save(self, *args, **kwargs):
        if not self.pk:
            self.from_email = self.from_email or settings.SERVER_EMAIL
            self.to_email = self.to_email or self.case.email
        if self.to_email:
            try:
                response = SendGridMail.send_template(self.from_email, self.to_email, self.data, self.template.tid)
                self.success = bool(response and response.status_code == 202)
            except SendGridMailTemplate.DoesNotExist as e:
                logger.error(e)
            super(SendGridMail, self).save(*args, **kwargs)

    def send(self):
        self.save()

    @staticmethod
    def send_template(from_email, to_email, data, template_id):
        """Call Sendgrid Transactional Template API"""
        sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
        if from_email == settings.SERVER_EMAIL:
            from_email = Email(from_email, name=settings.SERVER_EMAIL_NAME)
        else:
            from_email = Email(from_email)

        mail = Mail(from_email=from_email, to_email=Email(to_email))
        mail.personalizations[0].dynamic_template_data = json.loads(json.dumps(data, cls=DjangoJSONEncoder))
        mail.template_id = template_id
        try:
            return sg.client.mail.send.post(request_body=mail.get())
        except HTTPError as e:
            logger.error(e)
            return None
