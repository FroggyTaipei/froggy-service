from django.contrib import admin
from django.forms import ValidationError
from django.contrib.admin import ModelAdmin
from django.forms import TextInput, ModelForm
from django.utils.html import format_html
from django.urls import path, reverse
from suit_ckeditor.widgets import CKEditorWidget
from django.utils.translation import ugettext_lazy as _
from fsm_admin.mixins import FSMTransitionMixin
from suit.admin import SortableStackedInline
from suit.widgets import (
    EnclosedInput,
    AutosizedTextarea,
    SuitSplitDateTimeWidget,
)


from apps.cases.models import Type, Case
from apps.arranges.models import Arrange


class ArrangeInlineForm(ModelForm):
    class Meta:
        widgets = {
            'content': CKEditorWidget(attrs={'class': 'input-mini'}),
            'arrange_time': SuitSplitDateTimeWidget(),
        }

    def clean(self):
        new_state = self.cleaned_data['state']
        arrange_time = self.cleaned_data['arrange_time']

        if new_state != 'draft':
            if self.instance.case.state == 'draft':
                raise ValidationError(f'請先將案件由「尚未成案」設為「處理中」')
            if arrange_time is None:
                raise ValidationError(f'請先設定案件處理時間')
            else:
                self.instance.arrange_time = arrange_time

        transition = None
        for ts in self.instance.get_available_state_transitions():
            if new_state == ts.target:
                transition = ts

        if not transition and self.instance.state != new_state:
            raise ValidationError('您無法切換案件處理狀態為{new_state}')

        if transition:
            transition.method(self.instance)


class ArrangeInline(FSMTransitionMixin, SortableStackedInline):
    form = ArrangeInlineForm
    model = Arrange
    extra = 0
    verbose_name_plural = _('Arranges')
    suit_classes = 'suit-tab suit-tab-arranges'
    readonly_fields = ('publish_time',)


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
            'fields': ['username', 'email', 'mobile', 'address']}),
    ]

    suit_form_tabs = (
        ('general', _('General')),
        ('arranges', _('Arranges')),
        ('histories', _('Case Histories')),
        ('sendgrid_mails', _('Mails')),
    )

    suit_form_includes = (
        ('case_history_list.html', '', 'histories'),
        ('sendgrid_mail_list.html', '', 'sendgrid_mails'),
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Case, CaseAdmin)
admin.site.register(Type)
