from django.contrib import admin
from . import models


admin.site.register(models.TempFile)
admin.site.register(models.CaseFile)
