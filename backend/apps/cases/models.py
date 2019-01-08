from django.utils.translation import ugettext_lazy as _
from django.forms.models import model_to_dict
from django.utils import timezone
from django.db.models.signals import post_save
from django.db.models import (
    Model,
    CASCADE,
    CharField,
    DateTimeField,
    TextField,
    ForeignKey,
    EmailField,
    QuerySet,
    SET_NULL,
)
from django_fsm import FSMField, transition


class Type(Model):
    """案件類別"""
    name = CharField(max_length=50, verbose_name=_('Name'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    class Meta:
        verbose_name = _('Case Type')
        verbose_name_plural = _('Case Type')
        ordering = ('id',)

    def __str__(self):
        return self.name


class Region(Model):
    """使用者所在選區"""
    name = CharField(max_length=50, verbose_name=_('Name'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    class Meta:
        verbose_name = _('User Region')
        verbose_name_plural = _('User Region')
        ordering = ('id',)

    def __str__(self):
        return self.name


class State(object):
    """案件狀態"""
    DRAFT = 'draft'
    DISAPPROVED = 'disapproved'
    ARRANGED = 'arranged'
    CLOSED = 'closed'

    CHOICES = (
        (DRAFT, '尚未成案'),
        (DISAPPROVED, '不受理'),
        (ARRANGED, '處理中'),
        (CLOSED, '已結案'),
    )


class CaseQuerySet(QuerySet):
    """
    為了觸發post_save和pre_save，複寫Queryset的update函式，使用情境例如：
        Case.objects.filter(**kwargs).update(**kwargs)
    此改寫須迭代從資料庫取出、寫入物件，會導致時間複雜度比原生方法差上許多
        O(1) --> O(更新個數*更新欄位數)
    """
    def update(self, **kwargs):
        for case in self.all():
            for key, value in kwargs.items():
                setattr(case, key, value)
            case.save()


class Case(Model):
    """案件
    * state: 案件狀態, 預設值為未成案
    * case_id: 案件編號（6碼）
    * type: 案件類別
    * region: 使用者所在選區
    * title: 標題
    * content: 陳情內容
    * location: 相關地址
    * username: 使用者名字
    * mobile: 手機
    * email: 信箱
    * address: 地址
    * open_time: 成案日期
    * close_time: 結案日期
    * update_time: 上次更新時間
    """
    state = FSMField(default=State.DRAFT, verbose_name=_('Case State'), choices=State.CHOICES)
    number = CharField(max_length=6, verbose_name=_('Case Number'))
    type = ForeignKey('cases.Type', on_delete=CASCADE, related_name='cases', verbose_name=_('Case Type'))
    region = ForeignKey('cases.Region', on_delete=CASCADE, related_name='cases', verbose_name=_('User Region'))
    title = CharField(max_length=255, verbose_name=_('Case Title'))
    content = TextField(verbose_name=_('Content'))
    location = CharField(max_length=255, verbose_name=_('Location'))
    username = CharField(max_length=50, verbose_name=_('Username'))
    mobile = CharField(max_length=10, verbose_name=_('Mobile'))
    email = EmailField(verbose_name=_('Email'))
    address = CharField(max_length=255, verbose_name=_('Address'))
    open_time = DateTimeField(null=True, blank=True, verbose_name=_('Opened Time'))
    close_time = DateTimeField(null=True, blank=True, verbose_name=_('Closed Time'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    objects = CaseQuerySet.as_manager()

    class Meta:
        verbose_name = _('Case')
        verbose_name_plural = _('Cases')
        ordering = ('id',)

    def __init__(self, *args, **kwargs):
        super(Case, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.number

    def to_dict(self):
        """回傳去除id、將Foreign key轉為實例的字典"""
        model_dict = model_to_dict(self)
        model_dict.pop('id')
        # Foreign keys need to be instances via objects.create()
        model_dict['type'] = self.type
        model_dict['region'] = self.region
        return model_dict

    @property
    def first_history(self):
        """回傳最早的案件歷史，用於存取原始資料"""
        return self.case_histories.order_by('update_time').first()

    ########################################################
    # Transition Conditions
    # These must be defined prior to the actual transitions
    # to be reference.

    def can_arrange(self):
        return self.case_histories.all().count() > 1
    can_arrange.hint = '案件編輯過至少一次才能成案'

    def can_close(self):
        arranges = self.arranges.all()
        return arranges and all([arrange.published for arrange in arranges])
    can_close.hint = '全部的處理進度都發布後才能結案'

    ########################################################
    # Workflow (state) Transitions

    @transition(field=state, source=State.DRAFT, target=State.DISAPPROVED,
                custom={'button_name': '設為不受理'})
    def disapprove(self):
        self.close_time = timezone.now()

    @transition(field=state, source=State.DRAFT, target=State.ARRANGED, conditions=[can_arrange],
                custom={'button_name': '設為處理中'})
    def arrange(self):
        self.open_time = timezone.now()

    @transition(field=state, source=State.ARRANGED, target=State.CLOSED, conditions=[can_close],
                custom={'button_name': '設為已結案'})
    def close(self):
        self.close_time = timezone.now()


def case_mode_save(sender, instance, *args, **kwargs):
    """案件新增與每次更新時建立案件歷史"""
    history, created = CaseHistory.objects.get_or_create(case=instance, **instance.to_dict())
    if created:
        # Get editor via admin save_model()
        if hasattr(instance, 'user'):
            history.editor = instance.user
            history.save()


post_save.connect(case_mode_save, sender=Case)


class CaseHistory(Model):
    """案件歷史，案件新增與每次更新時建立"""
    editor = ForeignKey('users.User', null=True, blank=True, on_delete=SET_NULL, related_name='case_histories',
                        verbose_name=_('Editor'))
    case = ForeignKey('cases.Case', on_delete=CASCADE, related_name='case_histories', verbose_name=_('Case'))
    state = FSMField(default=State.DRAFT, verbose_name=_('Case State'), choices=State.CHOICES, protected=True)
    number = CharField(max_length=6, verbose_name=_('Case Number'))
    title = CharField(max_length=255, verbose_name=_('Case Title'))
    type = ForeignKey('cases.Type', on_delete=CASCADE, related_name='case_histories', verbose_name=_('Case Type'))
    region = ForeignKey('cases.Region', on_delete=CASCADE, related_name='case_histories', verbose_name=_('User Region'))
    content = TextField(verbose_name=_('Content'))
    location = CharField(max_length=255, verbose_name=_('Location'))
    username = CharField(max_length=50, verbose_name=_('Username'))
    mobile = CharField(max_length=10, verbose_name=_('Mobile'))
    email = EmailField(verbose_name=_('Email'))
    address = CharField(max_length=255, verbose_name=_('Address'))
    open_time = DateTimeField(null=True, blank=True, verbose_name=_('Opened Time'))
    close_time = DateTimeField(null=True, blank=True, verbose_name=_('Closed Time'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    class Meta:
        verbose_name = _('Case History')
        verbose_name_plural = _('Case Histories')
        ordering = ('-update_time',)

    def __str__(self):
        return self.number
