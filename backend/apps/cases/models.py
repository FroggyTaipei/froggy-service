from django.utils.translation import ugettext_lazy as _
from django.db.models import (
    Model,
    CASCADE,
    CharField,
    DateTimeField,
    TextField,
    ForeignKey,
    EmailField,
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


class Case(Model):
    """案件
    * status: 案件狀態
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
    status = ForeignKey('cases.Status', on_delete=CASCADE, verbose_name=_('Case Status'))
    case_id = CharField(max_length=6, verbose_name=_('Id'))
    type = ForeignKey('cases.Type', on_delete=CASCADE, verbose_name=_('Case Type'))
    region = ForeignKey('cases.Region', on_delete=CASCADE, verbose_name=_('User Region'))
    title = CharField(max_length=255, verbose_name=_('Title'))
    content = TextField(verbose_name=_('Content'))
    location = CharField(max_length=255, verbose_name=_('Location'))
    username = CharField(max_length=50, verbose_name=_('Username'))
    mobile = CharField(max_length=10, verbose_name=_('Mobile'))
    email = EmailField(verbose_name=_('Email'))
    open_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Opened Time'))
    close_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Closed Time'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    class Meta:
        verbose_name = _('Case')
        verbose_name_plural = _('Case')
        ordering = ('id',)

    def __str__(self):
        return self.case_id


class CaseHistory(Model):
    """案件歷史，案件新增與每次更新時建立"""
    status = ForeignKey('cases.Status', on_delete=CASCADE, verbose_name=_('Case Status'))
    case_id = CharField(max_length=6, verbose_name=_('Id'))
    title = CharField(max_length=255, verbose_name=_('Title'))
    type = ForeignKey('cases.Type', on_delete=CASCADE, verbose_name=_('Case Type'))
    region = ForeignKey('cases.Region', on_delete=CASCADE, verbose_name=_('User Region'))
    content = TextField(verbose_name=_('Content'))
    location = CharField(max_length=255, verbose_name=_('Location'))
    username = CharField(max_length=50, verbose_name=_('Username'))
    mobile = CharField(max_length=10, verbose_name=_('Mobile'))
    email = EmailField(verbose_name=_('Email'))
    open_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Opened Time'))
    close_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Closed Time'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    class Meta:
        verbose_name = _('Case History')
        verbose_name_plural = _('Case History')
        ordering = ('id',)

    def __str__(self):
        return self.case_id
