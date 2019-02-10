import datetime
import re
import calendar
from django.utils import timezone
from django.contrib import admin
from django.forms import ValidationError
from django.contrib.admin import ModelAdmin
from django.forms import TextInput, ModelForm, CharField
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from suit_ckeditor.widgets import CKEditorWidget
from fsm_admin.mixins import FSMTransitionMixin
from date_range_filter import DateRangeFilter
from suit.widgets import (
    EnclosedInput,
    AutosizedTextarea,
    SuitSplitDateTimeWidget,
)
from tagulous.forms import TagWidget

from apps.cases.models import Case, CaseHistory
from apps.arranges.models import Arrange
from apps.files.models import CaseFile


class ArrangeInlineForm(ModelForm):
    class Meta:
        widgets = {
            'content': CKEditorWidget(attrs={'class': 'input-mini'}),
            'arrange_time': SuitSplitDateTimeWidget(),
        }

    def clean(self):
        case_state = self.instance.case.state
        new_state = self.cleaned_data['state']
        arrange_time = self.cleaned_data['arrange_time']

        if new_state == 'published':
            if case_state == 'draft':
                raise ValidationError(f'新增處理事項前請先將案件由「尚未成案」設為「處理中」')
            if case_state == 'arranged' and self.instance.state == 'draft':
                if any(field in self.changed_data for field in ['title', 'content']):
                    raise ValidationError('請先儲存變動後再設為發布')
            if arrange_time is None:
                raise ValidationError(f'請先設定案件處理時間')
            else:
                self.instance.arrange_time = arrange_time

        if self.instance.pk is None and case_state == 'closed':
            raise ValidationError(f'新增處理事項前請先將案件由「已結案」設為「處理中」')

        transition = None
        for ts in self.instance.get_available_state_transitions():
            if new_state == ts.target:
                transition = ts

        if not transition and self.instance.state != new_state:
            raise ValidationError(f'您無法切換案件處理狀態為{new_state}')

        if transition:
            try:
                transition.method(self.instance)
            except Exception as e:
                raise ValidationError(e)


class ArrangeInline(FSMTransitionMixin, admin.StackedInline):
    form = ArrangeInlineForm
    model = Arrange
    extra = 0
    verbose_name_plural = _('Arranges')
    suit_classes = 'suit-tab suit-tab-arranges'

    def get_fields(self, request, obj=None):
        fields = ['state', 'title', 'content', 'arrange_time', 'publish_time']
        if not request.user.has_perm('arranges.add_arrange'):
            fields[2] = 'html_content'
        return fields

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ['publish_time']
        if not request.user.has_perm('arranges.add_arrange'):
            readonly_fields.append('context')
        return readonly_fields


class CaseFileInline(admin.TabularInline):
    model = CaseFile
    verbose_name_plural = _('Case File')
    suit_classes = 'suit-tab suit-tab-files'
    fields = ('file', 'type', 'preview', 'upload_time')
    readonly_fields = ('preview', 'upload_time')
    extra = 0


class CaseForm(ModelForm):
    class Meta:
        widgets = {
            'number': TextInput(attrs={'class': 'input-mini'}),
            'title': TextInput(attrs={'class': 'input-xxlarge'}),
            'content': AutosizedTextarea(attrs={'class': 'input-xxlarge'}),
            'location': TextInput(attrs={'class': 'input-xlarge'}),
            'username': EnclosedInput(append='icon-user', attrs={'class': 'input-small'}),
            'mobile': TextInput(attrs={'class': 'input-small'}),
            'email': EnclosedInput(append='icon-envelope', attrs={'class': 'input-medium'}),
            'disapprove_info': AutosizedTextarea(attrs={'class': 'input-xxlarge'}),
            'note': AutosizedTextarea(attrs={'class': 'input-xxlarge'}),
            'tags': TagWidget(attrs={'class': 'input-xxlarge'}),
        }
        help_texts = {
            'tags': '使用逗號分隔多個標籤',
        }

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if mobile:
            pattern = re.compile('^09\d{8}$')
            if not re.match(pattern, mobile):
                raise ValidationError('手機格式不正確')
            return mobile


class CaseAdmin(FSMTransitionMixin, ModelAdmin):
    form = CaseForm
    list_display = ('number', 'state', 'type', 'region', 'title', 'open_time', 'close_time')
    list_filter = (
        'type',
        'region',
        ('open_time', DateRangeFilter),
        ('close_time', DateRangeFilter),
    )
    list_select_related = True
    date_hierarchy = 'create_time'
    date_hierarchy_drilldown = False
    readonly_fields = ('number', 'state', 'create_time', 'open_time', 'close_time')
    ordering = ('-id',)
    fieldsets = [
        ('案件', {
            'classes': ('suit-tab suit-tab-general',),
            'description': '成案時間與結案時間在案件狀態更新時（已排程、已結案）自動紀錄',
            'fields': ['number', 'state', 'create_time', 'open_time', 'close_time'],
        }),
        ('案件資訊', {
            'classes': ('suit-tab suit-tab-general',),
            'description': '案件相關資訊',
            'fields': ['type', 'region', 'title', 'content', 'location'],
        }),
        ('案件人', {
            'classes': ('suit-tab suit-tab-general',),
            'description': '案件人個人資訊',
            'fields': ['username', 'mobile', 'email', 'address'],
        }),
        ('內部紀錄事項', {
            'classes': ('suit-tab suit-tab-general',),
            'description': '案件設為不受理前須填寫不受理理由',
            'fields': ['disapprove_info', 'note', 'tags'],
        }),
    ]

    inlines = (ArrangeInline, CaseFileInline)

    suit_form_includes = (
        ('case_history_list.html', '', 'histories'),
        ('sendgrid_mail_list.html', '', 'sendgrid_mails'),
    )

    class Media:
        """Django suit的DateFilter需要引用的外部資源"""
        js = ['/admin/jsi18n/']

    def get_form(self, request, obj=None, **kwargs):
        self._obj = obj
        return super(CaseAdmin, self).get_form(request, obj, **kwargs)

    @property
    def suit_form_tabs(self):
        obj = self._obj
        tabs = [
            ('general', _('General')),
            ('files', _('Files')),
            ('histories', _('Case Histories')),
        ]

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
            arranges = Arrange.objects.filter(
                Q(title__icontains=search_term)
                | Q(content__icontains=search_term),
            )
            arranges_ids = arranges.values_list('id', flat=True)
            histories = CaseHistory.objects.filter(
                Q(location__icontains=search_term)
                | Q(content__icontains=search_term)
                | Q(title__icontains=search_term)
                | Q(username__icontains=search_term)
                | Q(mobile__icontains=search_term)
                | Q(email__icontains=search_term),
            )
            histories_ids = histories.values_list('id', flat=True)
            queryset = queryset.filter(
                Q(arranges__id__in=arranges_ids)
                | Q(case_histories__id__in=histories_ids)
                | Q(number__icontains=search_term)
                | Q(disapprove_info__icontains=search_term)
                | Q(note__icontains=search_term),
            )

        return queryset, use_distinct

    def get_date_hierarchy_drilldown(self, year_lookup, month_lookup):
        """Drill-down only on past dates."""

        today = timezone.now().date()

        if year_lookup is None and month_lookup is None:
            # Past 3 years.
            return (
                datetime.date(y, 1, 1)
                for y in range(today.year - 2, today.year + 1)
            )

        elif year_lookup is not None and month_lookup is None:
            # Past months of selected year.
            this_month = today.replace(day=1)
            return (
                month for month in (
                    datetime.date(int(year_lookup), month, 1)
                    for month in range(1, 13)
                ) if month <= this_month
            )

        elif year_lookup is not None and month_lookup is not None:
            # Past days of selected month.
            days_in_month = calendar.monthrange(year_lookup, month_lookup)[1]
            return (
                day for day in (
                    datetime.date(year_lookup, month_lookup, i + 1)
                    for i in range(days_in_month)
                ) if day <= today
            )


admin.site.register(Case, CaseAdmin)
