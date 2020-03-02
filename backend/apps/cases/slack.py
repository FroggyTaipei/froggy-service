import logging
import json
from django.conf import settings
from slackclient import SlackClient

logger = logging.getLogger('raven')


def list_channels():
    """
    helper method for listing all slack channels
    """
    token = settings.SLACK_BOT_USER_TOKEN
    if not token:
        return {}
    sc = SlackClient(token)
    channels = sc.api_call('channels.list')
    # this is to make this function backwards-compatible with older version of SlackClient which returns a string
    if isinstance(channels, str):
        channels = json.loads(channels)
    return channels


def new_case_notify(case, channels=[], topic='froggyservice'):
    """
    helper method to post notify while new case is created.
    """

    context = f"""
有新的案件進來了！！ :tada: :tada:
標題： {case.title}
內容： {case.content}
點選連結前往編輯：
{case.admin_absolute_url}
    """
    token = settings.SLACK_BOT_USER_TOKEN
    if token:
        sc = SlackClient(token)
        channels = channels or list_channels()
        for channel in channels['channels']:
            if channel['topic']['value'] == topic:
                sc.api_call(
                    'chat.postMessage',
                    channel=channel['id'],
                    text=context,
                )
