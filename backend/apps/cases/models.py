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
    Q,
)


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


class Status(Model):
    """案件狀態"""
    name = CharField(max_length=50, verbose_name=_('Name'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    class Meta:
        verbose_name = _('Case Status')
        verbose_name_plural = _('Case Status')
        ordering = ('id',)

    def __str__(self):
        return self.name


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
    * status: 案件狀態, 預設值為未成案
    * case_id: 案件編號（6碼）
    * type: 案件類別
    * region: 使用者所在選區
    * title: 標題
    * content: 陳情內容
    * location: 相關地址
    * username: 使用者名字
    * mobile: 手機
    * email: 信箱
    * open_time: 成案日期
    * close_time: 結案日期
    * update_time: 上次更新時間
    """
    status = ForeignKey('cases.Status', on_delete=CASCADE, default=1,
                        related_name='cases', verbose_name=_('Case Status'))
    number = CharField(max_length=6, verbose_name=_('Case Number'))
    type = ForeignKey('cases.Type', on_delete=CASCADE, related_name='cases', verbose_name=_('Case Type'))
    region = ForeignKey('cases.Region', on_delete=CASCADE, related_name='cases', verbose_name=_('User Region'))
    title = CharField(max_length=255, verbose_name=_('Case Title'))
    content = TextField(verbose_name=_('Content'))
    location = CharField(max_length=255, verbose_name=_('Location'))
    username = CharField(max_length=50, verbose_name=_('Username'))
    mobile = CharField(max_length=10, verbose_name=_('Mobile'))
    email = EmailField(verbose_name=_('Email'))
    open_time = DateTimeField(null=True, blank=True, verbose_name=_('Opened Time'))
    close_time = DateTimeField(null=True, blank=True, verbose_name=_('Closed Time'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    objects = CaseQuerySet.as_manager()

    __original_status = None

    class Meta:
        verbose_name = _('Case')
        verbose_name_plural = _('Cases')
        ordering = ('id',)

    def __init__(self, *args, **kwargs):
        super(Case, self).__init__(*args, **kwargs)
        self.__original_status = self.status

    def __str__(self):
        return self.number

    def to_dict(self):
        """回傳去除id、Foreign key為實例的字典"""
        model_dict = model_to_dict(self)
        model_dict.pop('id')
        # Foreign keys need to be instances via objects.create()
        model_dict['status'] = self.status
        model_dict['type'] = self.type
        model_dict['region'] = self.region
        return model_dict

    @property
    def first_history(self):
        """回傳最早的案件歷史，用於存取原始資料"""
        return self.case_histories.order_by('update_time').first()

    def save(self, *args, **kwargs):
        """案件每次更新時檢查狀態、紀錄成案、結案時間戳"""
        if self.status != self.__original_status:
            if self.status.id == 2:  # 已排程
                self.open_time = timezone.now()
            if self.status.id in [4, 5]:  # 不受理、已結案
                self.close_time = timezone.now()
        self.__original_status = self.status
        super(Case, self).save(*args, **kwargs)


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
    status = ForeignKey('cases.Status', on_delete=CASCADE, related_name='case_histories', verbose_name=_('Case Status'))
    number = CharField(max_length=6, verbose_name=_('Case Number'))
    title = CharField(max_length=255, verbose_name=_('Case Title'))
    type = ForeignKey('cases.Type', on_delete=CASCADE, related_name='case_histories', verbose_name=_('Case Type'))
    region = ForeignKey('cases.Region', on_delete=CASCADE, related_name='case_histories', verbose_name=_('User Region'))
    content = TextField(verbose_name=_('Content'))
    location = CharField(max_length=255, verbose_name=_('Location'))
    username = CharField(max_length=50, verbose_name=_('Username'))
    mobile = CharField(max_length=10, verbose_name=_('Mobile'))
    email = EmailField(verbose_name=_('Email'))
    open_time = DateTimeField(null=True, blank=True, verbose_name=_('Opened Time'))
    close_time = DateTimeField(null=True, blank=True, verbose_name=_('Closed Time'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    class Meta:
        verbose_name = _('Case History')
        verbose_name_plural = _('Case Histories')
        ordering = ('-update_time',)

    def __str__(self):
        return self.number
