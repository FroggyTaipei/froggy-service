from django.utils.translation import ugettext_lazy as _
from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    BooleanField,
    PositiveIntegerField,
)


class MarqueeMessage(Model):
    """案件處理
    * message: 訊息
    * display: 是否顯示
    * update_time: 上次更新時間
    * order: 排序
    """
    message = CharField(max_length=255, verbose_name=_('Message'))
    display = BooleanField(default=True, verbose_name=_('Display'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    order = PositiveIntegerField(null=True, blank=True, verbose_name=_('Order'))

    class Meta:
        verbose_name = _('MarqueeMessage')
        verbose_name_plural = _('MarqueeMessage')
        ordering = ('order',)

    def __str__(self):
        return self.message
