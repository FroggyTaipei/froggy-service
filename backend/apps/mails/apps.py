from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MailsConfig(AppConfig):
    name = 'apps.mails'
    verbose_name = _('Mails')
