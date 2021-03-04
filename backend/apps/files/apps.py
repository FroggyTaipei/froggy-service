from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete


class FilesConfig(AppConfig):
    name = 'apps.files'
    verbose_name = _('Files')

    def ready(self):
        from . import models, signals
        post_delete.connect(signals.remove_file_from_storage, sender=models.CaseFile)
        post_delete.connect(signals.remove_file_from_storage, sender=models.TempFile)
