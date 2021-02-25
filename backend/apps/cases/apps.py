from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save


class CasesConfig(AppConfig):
    name = 'apps.cases'
    verbose_name = _('Cases')

    def ready(self):
        from . import models, signals
        post_save.connect(signals.create_history, sender=models.Case)
        post_save.connect(signals.new_case_notify, sender=models.Case)
