from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CasesConfig(AppConfig):
    name = 'apps.cases'
    verbose_name = _('Cases App')
