from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import TextInput, ModelForm
from suit_ckeditor.widgets import CKEditorWidget
from django.utils.translation import ugettext_lazy as _
from fsm_admin.mixins import FSMTransitionMixin
from suit.widgets import (
    SuitSplitDateTimeWidget,
    EnclosedInput,
    AutosizedTextarea,
)


from .models import Type, Case
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
    verbose_name_plural = _('Arranges')
    suit_classes = 'suit-tab suit-tab-arranges'


class CaseForm(ModelForm):
    class Meta:
        widgets = {
            'number': TextInput(attrs={'class': 'input-mini'}),
            'content': AutosizedTextarea,
            'username': EnclosedInput(append='icon-user', attrs={'class': 'input-small'}),
            'email': EnclosedInput(append='icon-envelope', attrs={'class': 'input-small'}),
        }


class CaseAdmin(FSMTransitionMixin, ModelAdmin):
    form = CaseForm
    search_fields = ('number',)
    list_display = ('number', 'state', 'type', 'region', 'title', 'open_time', 'close_time')
    list_filter = ('type', 'region')
    readonly_fields = ('state', 'open_time', 'close_time')
    list_select_related = True

    inlines = (ArrangeInline,)

    fieldsets = [
        (_('Case'), {
            'classes': ('suit-tab suit-tab-general',),
            'description': _('Case open time and close time base on case state.'),
            'fields': ['number', 'state', 'open_time', 'close_time'],
        }),
        (_('Information'), {
            'classes': ('suit-tab suit-tab-general',),
            'description': _('Case Information'),
            'fields': ['type', 'region', 'title', 'content', 'location']}),
        (_('Proposer'), {
            'classes': ('suit-tab suit-tab-general',),
            'description': _('Proposer Information'),
            'fields': ['username', 'email', 'mobile']}),
    ]

    suit_form_tabs = (
        ('general', _('General')),
        ('arranges', _('Arranges')),
        ('histories', _('Case Histories')),
    )

    suit_form_includes = (
        ('case_history_list.html', '', 'histories'),
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Case, CaseAdmin)
admin.site.register(Type)
