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
        new_state = self.cleaned_data['state']
        arrange_time = self.cleaned_data['arrange_time']

        if any(field in self.changed_data for field in ['title', 'content']) and new_state == 'published':
            raise ValidationError('請先儲存變動後再設為發布')

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
    fields = ('state', 'title', 'content', 'arrange_time', 'publish_time')
    readonly_fields = ('publish_time',)

    def has_add_permission(self, request, obj=None):
        return request.user.has_perm('arranges.add_arrange') and obj and obj.state == 'arranged'

    def has_view_permission(self, request, obj=None):
        return request.user.has_perm('arranges.view_arrange') and obj and obj.state in ['arranged', 'closed']

    def get_fields(self, request, obj=None):
        if not request.user.has_perm('arranges.add_arrange'):
            return 'state', 'title', 'html_content', 'arrange_time', 'publish_time'
        return self.fields

    def get_readonly_fields(self, request, obj=None):
        if not request.user.has_perm('arranges.add_arrange'):
            return self.readonly_fields + ('html_content',)
        return self.readonly_fields


class CaseFileInline(admin.TabularInline):
    model = CaseFile
    verbose_name_plural = _('Case File')
    suit_classes = 'suit-tab suit-tab-files'
    fields = ('file', 'preview', 'upload_time')
    readonly_fields = ('preview', 'upload_time')
    extra = 0


class CaseForm(ModelForm):
    mobile = CharField(max_length=10, required=False, label=_('Mobile'))

    class Meta:
        widgets = {
            'number': TextInput(attrs={'class': 'input-mini'}),
            'title': TextInput(attrs={'class': 'input-xxlarge'}),
            'content': AutosizedTextarea(attrs={'class': 'input-xxlarge'}),
            'location': TextInput(attrs={'class': 'input-xlarge'}),
            'username': EnclosedInput(append='icon-user', attrs={'class': 'input-small'}),
            'mobile': TextInput(attrs={'class': 'input-mini'}),
            'email': EnclosedInput(append='icon-envelope', attrs={'class': 'input-medium'}),
            'disapprove_info': AutosizedTextarea(attrs={'class': 'input-xxlarge'}),
            'note': AutosizedTextarea(attrs={'class': 'input-xxlarge'}),
            'tags': TagWidget(attrs={'class': 'input-xxlarge'}),
        }
        help_texts = {
            'tags': '使用逗號分隔多個標籤',
        }

    def clean(self):
        pattern = re.compile('^09\d{8}$')
        if 'mobile' in self.changed_data:
            mobile = self.cleaned_data['mobile']
            if not re.match(pattern, mobile):
                raise ValidationError('手機格式不正確')
            self.cleaned_data['mobile'] = f'+886{mobile[1:]}'
            self.instance.mobile = f'+886{mobile[1:]}'
            return self.cleaned_data


class CaseAdmin(FSMTransitionMixin, ModelAdmin):
    form = CaseForm
    search_fields = ('id', 'number', 'title')
    list_display = ('number', 'state', 'type', 'region', 'title', 'open_time', 'close_time')
    list_filter = (
        'type',
        'region',
        ('open_time', DateRangeFilter),
        ('close_time', DateRangeFilter),
    )
    readonly_fields = ('number', 'state', 'create_time', 'open_time', 'close_time')
    list_select_related = True
    date_hierarchy = 'create_time'
    date_hierarchy_drilldown = False

    inlines = (ArrangeInline, CaseFileInline)

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

    suit_form_includes = (
        ('case_history_list.html', '', 'histories'),
        ('sendgrid_mail_list.html', '', 'sendgrid_mails'),
        # ('files_list.html', '', 'files'),
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
            ('files', _('Case File')),
        ]

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

    def get_fieldsets(self, request, obj=None):
        """若是已新增過的物件，以tw_mobile取代mobile input"""
        if obj:
            fieldsets = self.fieldsets
            fieldsets[2][1]['fields'] = ['username', 'tw_mobile', 'email', 'address']
            return fieldsets
        return self.fieldsets

    def get_readonly_fields(self, request, obj=None):
        """若是已新增過的物件，以tw_mobile取代mobile input，設為readonly"""
        if obj:
            return self.readonly_fields + ('tw_mobile',)
        return self.readonly_fields

    def get_fields(self, request, obj=None):
        """若是已新增過的物件，以tw_mobile取代mobile input，設為readonly，加到fields當中"""
        if obj:
            return self.fields + ('tw_mobile',)
        return self.fields

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
