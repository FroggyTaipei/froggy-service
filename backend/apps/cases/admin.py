from django.contrib import admin
from django.forms import ValidationError
from django.contrib.admin import ModelAdmin
from django.forms import TextInput, ModelForm
from django.db.models import Q
from suit_ckeditor.widgets import CKEditorWidget
from django.utils.translation import ugettext_lazy as _
from fsm_admin.mixins import FSMTransitionMixin
from suit.admin import SortableStackedInline
from suit.widgets import (
    EnclosedInput,
    AutosizedTextarea,
    SuitSplitDateTimeWidget,
)


from apps.cases.models import Case, CaseHistory
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
            raise ValidationError(f'您無法切換案件處理狀態為{new_state}')

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
            'title': TextInput(attrs={'class': 'input-xxlarge'}),
            'content': AutosizedTextarea(attrs={'class': 'input-xxlarge'}),
            'location': TextInput(attrs={'class': 'input-xlarge'}),
            'username': EnclosedInput(append='icon-user', attrs={'class': 'input-small'}),
            'mobile': EnclosedInput(attrs={'class': 'input-small'}),
            'email': EnclosedInput(append='icon-envelope', attrs={'class': 'input-medium'}),
            'disapprove_info': AutosizedTextarea(attrs={'class': 'input-xxlarge'}),
            'close_info': AutosizedTextarea(attrs={'class': 'input-xxlarge'}),
        }


class CaseAdmin(FSMTransitionMixin, ModelAdmin):
    form = CaseForm
    search_fields = ('id',)
    list_display = ('number', 'state', 'type', 'region', 'title', 'open_time', 'close_time')
    list_filter = ('type', 'region')
    readonly_fields = ('number', 'state', 'create_time', 'open_time', 'close_time')
    list_select_related = True

    inlines = (ArrangeInline,)

    fieldsets = [
        (_('Case'), {
            'classes': ('suit-tab suit-tab-general',),
            'description': '成案時間與結案時間在案件狀態更新時（已排程、已結案）自動紀錄',
            'fields': ['number', 'state', 'create_time', 'open_time', 'close_time'],
        }),
        (_('Information'), {
            'classes': ('suit-tab suit-tab-general',),
            'description': '案件相關資訊',
            'fields': ['type', 'region', 'title', 'content', 'location'],
        }),
        (_('Proposer'), {
            'classes': ('suit-tab suit-tab-general',),
            'description': '陳情人個人資訊',
            'fields': ['username', 'mobile', 'email', 'address'],
        }),
        (_('Case Close Information'), {
            'classes': ('suit-tab suit-tab-general',),
            'description': '結案理由，案件設為不受理前須填寫',
            'fields': ['disapprove_info', 'close_info'],
        }),
    ]

    suit_form_includes = (
        ('case_history_list.html', '', 'histories'),
        ('sendgrid_mail_list.html', '', 'sendgrid_mails'),
        ('files_list.html', '', 'files'),
    )

    def get_form(self, request, obj=None, **kwargs):
        self._obj = obj
        return super(CaseAdmin, self).get_form(request, obj, **kwargs)

    @property
    def suit_form_tabs(self):
        obj = self._obj
        tabs = [
            ('general', _('General')),
        ]

        if obj and obj.casefiles.count() > 0:
            tabs.append(('files', _('Files')))

        tabs.append(('histories', _('Case Histories')))

        if obj and obj.state in ['arranged', 'closed']:
            tabs.append(('arranges', _('Arranges')))

        if obj and obj.sendgrid_mails.count() > 0:
            tabs.append(('sendgrid_mails', _('Mails')))

        return tabs

    def save_model(self, request, obj, form, change):
        """於post_save時取得編輯者"""
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_search_results(self, request, queryset, search_term):
        """加入CaseHistory搜尋"""
        queryset, use_distinct = super(CaseAdmin, self).get_search_results(request, queryset, search_term)

        if search_term:
            histories = CaseHistory.objects.filter(
                Q(location__icontains=search_term)
                | Q(content__icontains=search_term)
                | Q(title__icontains=search_term)
                | Q(username__icontains=search_term)
                | Q(mobile__icontains=search_term)
                | Q(email__icontains=search_term),
            )
            histories_ids = histories.values_list('case__id', flat=True)
            queryset = queryset.filter(
                Q(id__in=[histories_ids])
                | Q(number__icontains=search_term)
                | Q(disapprove_info__icontains=search_term)
                | Q(close_info__icontains=search_term),
            )

        return queryset, use_distinct


admin.site.register(Case, CaseAdmin)
