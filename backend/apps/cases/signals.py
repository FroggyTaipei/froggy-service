import logging
from .models import Case, CaseHistory


def create_history(sender, instance: Case, **kwargs):
    history, history_created = CaseHistory.objects.get_or_create(case=instance, **instance.to_dict())
    if history_created:
        # Get editor via admin save_model()
        if hasattr(instance, 'user'):
            history.editor = instance.user
            history.save()


def new_case_notify(sender, instance: Case, created, **kwargs):
    from . import slack
    if created:
        try:
            slack.new_case_notify(instance)
        except Exception as exc:
            logging.exception(exc)
