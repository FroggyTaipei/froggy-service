from django.contrib import admin
from . import models


class CaseFileAdmin(admin.ModelAdmin):
    list_display = ('case', 'file_name', 'type', 'upload_time')
    list_filter = ('type',)
    search_fields = (
        'file_name',
        'case__id',
    )


admin.site.register(models.CaseFile, CaseFileAdmin)
