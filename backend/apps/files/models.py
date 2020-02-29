import uuid
import datetime
import imghdr

from django.db import models
from django.db.models.signals import pre_delete
from django.core.files.base import ContentFile
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.safestring import mark_safe

from rest_framework.exceptions import ValidationError

from .storages import CaseStorage, TempStorage


class FileType(object):
    CASE = 'case'
    ARRANGE = 'arrange'

    CHOICES = (
        ('case', '案件附件'),
        ('arrange', '處理紀錄附件'),
    )


class TempFile(models.Model):
    """
    暫存檔案
    * case: 案件編號，因案件未成立，先以字串紀錄
    * file: 案件檔案，storage指定到 TEMP
    * file_name: 案件檔案名稱，不可編輯，save()時自動產生
    * upload_time: 檔案上傳時間
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tempfiles', verbose_name=_('Temp File'))
    case_uuid = models.UUIDField(verbose_name=_('UUID'))
    file = models.FileField(storage=TempStorage(), verbose_name=_('Temp file'))
    file_name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('File Name'))
    size = models.PositiveIntegerField(editable=False, verbose_name=_('Size'))
    upload_time = models.DateTimeField(auto_now=True, verbose_name=_('Upload Time'))

    class Meta:
        verbose_name = _('Temp File')
        verbose_name_plural = _('Temp File')

    def __str__(self):
        return f'{self.case_uuid} - {self.file_name}'

    @property
    def url(self):
        return self.file.url

    def check_duplicate(self):
        """
        檢查案件編號及檔案名稱是否重複
        """
        return TempFile.objects.filter(case_uuid=self.case_uuid, file_name=self.file_name).count() > 0

    def check_size_per_file(self):
        """
        檢查上傳的檔案大小是否超過大小限制
        """
        return self.size > settings.FILE_LIMIT_PER_FILE

    def check_size_per_case(self):
        """
        檢查已上傳案件的總大小與目前上傳的檔案相加是否超過限制
        """
        total = self.size + sum(TempFile.objects.filter(case_uuid=self.case_uuid).values_list('size', flat=True))

        return total > settings.FILE_LIMIT_PER_CASE

    def check_size_per_day(self):
        """
        檢查今日上傳的總檔案大小是否達到今日上傳的總額度
        """
        total = self.size + \
            sum(TempFile.objects.filter(user=self.user,
                                        upload_time__date=datetime.date.today()).values_list('size', flat=True))
        return total > settings.FILE_LIMIT_PER_DAY

    def save(self, *args, **kwargs):
        self.file_name = self.file.name
        self.size = self.file.size
        if self.check_duplicate():
            raise ValidationError('相同檔名的檔案已經存在')
        if self.check_size_per_file():
            raise ValidationError('單一檔案大小超出限制')
        if self.check_size_per_case():
            raise ValidationError('單一案件的上傳檔案大小超出限制')
        if self.check_size_per_day():
            raise ValidationError('您的手機號碼已超出上傳限制，請聯絡本團隊為您處理')
        self.file.name = f'{self.case_uuid}/{self.file_name}'
        super(TempFile, self).save(*args, **kwargs)

    def migrate_to_case(self, case):
        new_file = ContentFile(self.file.read())
        new_file.name = self.file.name
        CaseFile.objects.create(
            case=case,
            file=new_file,
            file_name=self.file_name
        )
        self.delete()


class CaseFile(models.Model):
    """
    案件檔案
    * case: 案件編號
    * file: 案件檔案
    * file_name: 案件檔案名稱(自動產生)
    * upload_time: 檔案上傳時間
    """
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='casefiles', verbose_name=_('Case File'))
    type = models.CharField(max_length=20, default=FileType.CASE, choices=FileType.CHOICES, verbose_name=_('File Type'))
    file = models.FileField(storage=CaseStorage(), verbose_name=_('Case File'))
    file_name = models.CharField(max_length=255, null=True, blank=True, editable=False, verbose_name=_('File Name'))
    upload_time = models.DateTimeField(auto_now=True, verbose_name=_('Upload Time'))

    class Meta:
        verbose_name = _('Case File')
        verbose_name_plural = _('Case File')
        ordering = ('-type', '-upload_time')

    def __str__(self):
        return f'{self.case} - {self.file_name}'

    @property
    def url(self):
        return self.file.url

    def preview(self):
        if not self.file_name:
            return '-'
        if imghdr.what(self.file):
            return mark_safe(f"""
                <a target="_blank" href="{self.file.url}"><img src="{self.file.url}" style="max-width: 200px"/></a>
            """)
        return mark_safe(f'<a target="_blank" href="{self.file.url}">{self.file_name}</a>')
    preview.short_description = _('Preview')


@receiver(pre_delete, sender=TempFile)
def temp_file_delete_handler(sender, instance, **kwargs):
    instance.file.storage.delete(name=instance.file.name)


@receiver(pre_delete, sender=CaseFile)
def case_file_delete_handler(sender, instance, **kwargs):
    instance.file.storage.delete(name=instance.file.name)
