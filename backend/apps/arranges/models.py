from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    ForeignKey,
    CASCADE,
    PositiveIntegerField,
)
from django_fsm import FSMField, transition
from ckeditor_uploader.fields import RichTextUploadingField


class State(object):
    """案件狀態"""
    DRAFT = 'draft'               # 尚未發布
    PUBLISHED = 'published'       # 以發布
    REPUBLISHED = 'republished'   # 已重新發布

    CHOICES = (
        (DRAFT, _('Arrange Draft')),
        (PUBLISHED, _('Published')),
        (REPUBLISHED, _('Republished')),
    )


class Arrange(Model):
    """案件處理
    * case: 案件
    * title: 案件處理標題
    * state: 案件處理狀態
    * content: 案件處理內容
    * time: 案件處理時間
    * update_time: 上次更新時間
    """
    state = FSMField(default=State.DRAFT, verbose_name=_('Arrange State'), choices=State.CHOICES)
    case = ForeignKey('cases.Case', on_delete=CASCADE, related_name='arranges', verbose_name=_('Case'))
    title = CharField(max_length=120, verbose_name=_('Arrange Title'))
    content = RichTextUploadingField(verbose_name=_('Content'))
    publish_time = DateTimeField(null=True, blank=True, verbose_name=_('Arrange Publish Time'))
    update_time = DateTimeField(auto_now=True, null=True, blank=True, verbose_name=_('Updated Time'))

    order = PositiveIntegerField()

    class Meta:
        verbose_name = _('Arrange')
        verbose_name_plural = _('Arrange')
        ordering = ('order',)

    def __str__(self):
        return f'{self.case.number}-{self.title}'

    @property
    def number(self):
        return self.case.number

    ########################################################
    # Transition Conditions
    # These must be defined prior to the actual transitions
    # to be refrenced.

    ########################################################
    # Workflow (state) Transitions

    @transition(field=state, source=State.DRAFT, target=State.PUBLISHED,
                custom={'button_name': _('Publish this arrange')})
    def publish(self):
        """"""
        self.publish_time = timezone.now()

    @transition(field=state, source=State.PUBLISHED, target=State.REPUBLISHED,
                custom={'button_name': _('Republish this arrange')})
    def republish(self):
        """"""
        self.publish_time = timezone.now()
