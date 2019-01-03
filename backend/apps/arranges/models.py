from django.utils.translation import ugettext_lazy as _
from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    ForeignKey,
    CASCADE,
)
from ckeditor_uploader.fields import RichTextUploadingField


class Arrange(Model):
    """案件處理
    * case: 案件
    * title: 案件處理標題
    * content: 案件處理內容
    * time: 案件處理時間
    * update_time: 上次更新時間
    """
    case = ForeignKey('cases.Case', on_delete=CASCADE, related_name='arranges', verbose_name=_('Case'))
    title = CharField(max_length=120, verbose_name=_('Title'))
    content = RichTextUploadingField(verbose_name=_('Content'))
    time = DateTimeField(auto_now=True, verbose_name=_('Arranged Time'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    class Meta:
        verbose_name = _('Arrange')
        verbose_name_plural = _('Arrange')
        ordering = ('id',)

    def __str__(self):
        return f'{self.case.case_id}-{self.title}'
