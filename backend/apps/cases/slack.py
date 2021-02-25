from django.conf import settings
from slack_sdk import WebClient


def new_case_notify(case, topic='froggyservice'):
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
        sc = WebClient(token)
        channels = sc.conversations_list()['channels']
        for channel in channels:
            if channel['topic']['value'] == topic:
                sc.chat_postMessage(channel=channel['id'], text=context)
