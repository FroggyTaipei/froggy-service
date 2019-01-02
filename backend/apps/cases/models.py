from django.utils.translation import ugettext_lazy as _
from django.db.models import (
    Model,
    CASCADE,
    CharField,
    DateTimeField,
    TextField,
    ForeignKey,
    EmailField,
    DateField,
)


class Type(Model):
    """Case type"""
    name = CharField(max_length=50, verbose_name=_('Name'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated'))

    class Meta:
        verbose_name = _('Case Type')
        verbose_name_plural = _('Case Type')
        ordering = ('id',)

    def __str__(self):
        return self.name


class Region(Model):
    """User region"""
    name = CharField(max_length=50, verbose_name=_('Name'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated'))

    class Meta:
        verbose_name = _('User Region')
        verbose_name_plural = _('User Region')
        ordering = ('id',)

    def __str__(self):
        return self.name


class Status(Model):
    """Case status"""
    name = CharField(max_length=50, verbose_name=_('Name'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated'))

    class Meta:
        verbose_name = _('Case Status')
        verbose_name_plural = _('Case Status')
        ordering = ('id',)

    def __str__(self):
        return self.name


class Case(Model):
    """Case"""
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
    open_date = DateField(auto_now=True, verbose_name=_('Open Date'))
    close_date = DateField(auto_now=True, null=True, blank=True, verbose_name=_('Close Date'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated'))

    class Meta:
        verbose_name = _('Case')
        verbose_name_plural = _('Case')
        ordering = ('id',)

    def __str__(self):
        return self.case_id


class CaseHistory(Model):
    """Case history, create via case create/update, delete via case delete"""
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
    open_date = DateField(auto_now=True, verbose_name=_('Open Date'))
    close_date = DateField(auto_now=True, null=True, blank=True, verbose_name=_('Close Date'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated'))

    class Meta:
        verbose_name = _('Case History')
        verbose_name_plural = _('Case History')
        ordering = ('id',)

    def __str__(self):
        return self.case_id
