import time
import re
import jieba
from jieba import analyse
from collections import Counter
from _datetime import datetime
from dateutil.rrule import rrule, MONTHLY

from django.db.models import Count
from django.db.models.functions import TruncMonth, TruncYear
from django.conf import settings

from apps.cases.models import Case, State, Region, Type
from config.charts import (
    get_highchart_pie,
    get_highchart_line,
    get_highchart_word_cloud,
)


def months(start_month, start_year, end_month, end_year):
    start = datetime(start_year, start_month, 1)
    end = datetime(end_year, end_month, 1)
    return [(d.month, d.year) for d in rrule(MONTHLY, dtstart=start, until=end)]


def to_unix(datetime):
    return int(time.mktime(datetime.timetuple()) * 1000)


def case_state_pie():
    data = []
    qs = Case.objects.all()
    if qs:
        for i, (state, title) in enumerate(State.CHOICES):
            y = qs.filter(state=state).count() / qs.count()
            data.append(
                {
                    'name': title,
                    'y': y,
                },
            )
        data = sorted(data, key=lambda x: x['y'], reverse=True)
        data[0]['sliced'] = True
        data[0]['selected'] = True

    chart = get_highchart_pie(data=data)
    return chart


def case_region_pie():
    data = []
    qs = Case.objects.all()
    if qs:
        for region in Region.objects.all():
            y = qs.filter(region=region).count() / qs.count()
            data.append(
                {
                    'name': region.name,
                    'y': y,
                },
            )
        data = sorted(data, key=lambda x: x['y'], reverse=True)
        data[0]['sliced'] = True
        data[0]['selected'] = True

    chart = get_highchart_pie(data=data)
    return chart


def case_type_pie():
    data = []
    qs = Case.objects.all()
    if qs:
        for type_ in Type.objects.all():
            y = qs.filter(type=type_).count() / qs.count()
            data.append(
                {
                    'name': type_.name,
                    'y': y,
                },
            )
        data = sorted(data, key=lambda x: x['y'], reverse=True)
        data[0]['sliced'] = True
        data[0]['selected'] = True

    chart = get_highchart_pie(data=data)
    return chart


def case_type_line_monthly():
    qs = Case.objects.annotate(
        year=TruncYear('create_time'),
        month=TruncMonth('create_time'),
    ).values('month', 'type').annotate(
        count=Count('id'),
    ).values('month', 'type__name', 'count').order_by('month')

    result = {type_.name: [] for type_ in Type.objects.all()}

    for item in qs:
        result[item['type__name']].append([to_unix(item['month']), item['count']])

    data = [{'name': key, 'data': value} for key, value in result.items()]

    chart = get_highchart_line(data=data, y_title='案件類型')

    return chart


def case_region_line_monthly():
    qs = Case.objects.annotate(
        year=TruncYear('create_time'),
        month=TruncMonth('create_time'),
    ).values('month', 'type').annotate(
        count=Count('id'),
    ).values('month', 'region__name', 'count').order_by('month')

    result = {region.name: [] for region in Region.objects.all()}

    for item in qs:
        result[item['region__name']].append([to_unix(item['month']), item['count']])

    data = [{'name': key, 'data': value} for key, value in result.items()]

    chart = get_highchart_line(data=data, y_title='選區')

    return chart


def case_content_wordcloud():
    content = ''
    for case in Case.objects.all():
        content += case.first_history.content
        content += case.first_history.title

    jieba.set_dictionary(str(settings.ROOT_DIR('static/dict.txt')))

    pattern = re.compile('[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？“”、~@#￥%……&*（）(\d+)]+')
    content = pattern.sub("", content)

    words = [word for word in jieba.cut_for_search(content) if len(word) > 2]
    counter = Counter(words)
    data = [{'name': word, 'weight': weight} for word, weight in counter.most_common(20)]

    chart = get_highchart_word_cloud(data=data)

    return chart
