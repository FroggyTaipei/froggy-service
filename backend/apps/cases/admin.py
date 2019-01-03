from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import TextInput, ModelForm
from suit_ckeditor.widgets import CKEditorWidget
from suit.widgets import (
    SuitSplitDateTimeWidget,
    EnclosedInput,
    AutosizedTextarea,
)


from .models import Case
from apps.arranges.models import Arrange


class ArrangeInlineForm(ModelForm):
    class Meta:
        widgets = {
            'content': CKEditorWidget(attrs={'class': 'input-mini'}),
            'time': SuitSplitDateTimeWidget,
        }


class ArrangeInline(admin.TabularInline):
    form = ArrangeInlineForm
    model = Arrange
    extra = 1
    verbose_name_plural = 'Arranges'
    suit_classes = 'suit-tab suit-tab-arranges'


class CaseForm(ModelForm):
    class Meta:
        widgets = {
            'number': TextInput(attrs={'class': 'input-mini'}),
            'content': AutosizedTextarea,
            'username': EnclosedInput(append='icon-user', attrs={'class': 'input-small'}),
            'email': EnclosedInput(append='icon-envelope', attrs={'class': 'input-small'}),
        }


class CaseAdmin(ModelAdmin):
    form = CaseForm
    search_fields = ('number',)
    list_display = ('number', 'status', 'type', 'region', 'title', 'open_time', 'close_time')
    list_filter = ('type', 'region')
    readonly_fields = ('open_time', 'close_time')
    list_select_related = True

    inlines = (ArrangeInline,)

    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['number', 'status', 'open_time', 'close_time'],
        }),
        ('Information', {
            'classes': ('suit-tab suit-tab-general',),
            'description': 'Case Information',
            'fields': ['type', 'region', 'title', 'content', 'username', 'location']}),
    ]

    suit_form_tabs = (
        ('general', 'General'),
        ('arranges', 'Arranges'),
        ('histories', 'CaseHistories'),
    )

    suit_form_includes = (
        ('case_history_list.html', '', 'histories'),
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Case, CaseAdmin)
