import time
import re
import jieba
from itertools import accumulate
from collections import Counter

from django.db.models import Count
from django.db.models.functions import TruncDate, TruncYear
from django.conf import settings

from apps.cases.models import Case, State, Region


__all__ = [
    'get_case_state_pie_data',
    'get_case_region_pie_data',
    'get_case_type_pie_data',
    'get_case_state_packed_bubble_data',
    'get_case_region_packed_bubble_data',
    'get_case_type_packed_bubble_data',
    'get_case_line_data',
    'get_case_type_line_data',
    'get_case_region_line_data',
    'get_case_content_wordcloud_data'
]


def to_unix(dt):
    return int(time.mktime(dt.timetuple()) * 1000)


def get_case_state_pie_data():
    total = Case.objects.count()
    qs = Case.objects.values('state').order_by().annotate(count=Count('id'))
    data = [
        {
            'name': title,
            'y': qs.get(state=state)['count'] / total
        } for state, title in State.CHOICES
    ]
    if data:
        data = sorted(data, key=lambda x: x['y'], reverse=True)
        data[0]['sliced'] = True
        data[0]['selected'] = True
    return data


def get_case_region_pie_data():
    total = Case.objects.count()
    qs = Case.objects.values('region__name').order_by().annotate(count=Count('id'))
    data = [
        {
            'name': item['region__name'],
            'y': item['count'] / total
        } for item in qs
    ]
    if data:
        data = sorted(data, key=lambda x: x['y'], reverse=True)
        data[0]['sliced'] = True
        data[0]['selected'] = True
    return data


def get_case_type_pie_data():
    total = Case.objects.count()
    qs = Case.objects.values('type__name').order_by().annotate(count=Count('id'))
    data = [
        {
            'name': item['type__name'],
            'y': item['count'] / total
        } for item in qs
    ]
    if data:
        data = sorted(data, key=lambda x: x['y'], reverse=True)
        data[0]['sliced'] = True
        data[0]['selected'] = True
    return data


def get_case_state_packed_bubble_data():
    qs = Case.objects.values('state').order_by().annotate(count=Count('id'))
    return [
        {
            'name': title,
            'data': [{
                'name': title,
                'value': qs.get(state=state)['count']
            }]
        } for state, title in State.CHOICES
    ]


def get_case_region_packed_bubble_data():
    qs = Case.objects.values('region__name').order_by().annotate(count=Count('id'))
    return [
        {
            'name': item['region__name'],
            'data': [{
                'name': item['region__name'],
                'value': item['count']
            }]
        } for item in qs
    ]


def get_case_type_packed_bubble_data():
    qs = Case.objects.values('type__name').order_by().annotate(count=Count('id'))
    return [
        {
            'name': item['type__name'],
            'data': [{
                'name': item['type__name'],
                'value': item['count']
            }]
        } for item in qs
    ]


def get_case_line_data(accumulative=True):
    qs = Case.objects.annotate(
        year=TruncYear('create_time'),
        date=TruncDate('create_time'),
    ).values('date').annotate(
        count=Count('id'),
    ).order_by('date')
    dates = []
    counts = []
    for item in qs:
        dates.append(to_unix(item['date']))
        counts.append(item['count'])
    if accumulative:
        counts = list(accumulate(counts))
    data = [list(t) for t in zip(dates, counts)]
    return [
        {
            'name': '全部',
            'data': data
        }
    ]


def get_case_type_line_data(accumulative=True):
    qs = Case.objects.annotate(
        year=TruncYear('create_time'),
        date=TruncDate('create_time'),
    ).values('date', 'type__name').annotate(
        count=Count('id'),
    ).order_by('date')

    results = []
    for name in set(qs.values_list('type__name', flat=True)):
        dates = []
        counts = []
        for item in qs.filter(type__name=name):
            dates.append(to_unix(item['date']))
            counts.append(item['count'])
        if accumulative:
            counts = list(accumulate(counts))
        results.append({
            'name': name,
            'data': [list(t) for t in zip(dates, counts)]
        })

    return results


def get_case_region_line_data(accumulative=True):
    qs = Case.objects.annotate(
        year=TruncYear('create_time'),
        date=TruncDate('create_time'),
    ).values('date', 'region__name').annotate(
        count=Count('id'),
    ).order_by('date')

    results = []
    for name in set(qs.values_list('region__name', flat=True)):
        dates = []
        counts = []
        for item in qs.filter(region__name=name):
            dates.append(to_unix(item['date']))
            counts.append(item['count'])
        if accumulative:
            counts = list(accumulate(counts))
        results.append({
            'name': name,
            'data': [list(t) for t in zip(dates, counts)]
        })

    return results


def get_case_content_wordcloud_data():
    content = ''
    for case in Case.objects.all():
        content += case.first_history.content
        content += case.first_history.title

    jieba.set_dictionary(str(settings.ROOT_DIR('static/jieba/dict.txt')))
    stop = []
    with open(str(settings.ROOT_DIR('static/jieba/stop.txt')), 'r', encoding='UTF-8') as file:
        for data in file.readlines():
            data = data.strip()
            stop.append(data)

    pattern = re.compile(r'[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？“”、~@#￥%……&*（）(\d+)]+')
    content = pattern.sub("", content)

    words_2 = [word for word in jieba.cut_for_search(content) if len(word) == 2 and word not in stop]
    counter_2 = Counter(words_2)

    words_3 = [word for word in jieba.cut_for_search(content) if len(word) > 2 and word not in stop]
    counter_3 = Counter(words_3)

    data = [{'name': word, 'weight': weight*1} for word, weight in counter_2.most_common(20)] + \
           [{'name': word, 'weight': weight*1.5} for word, weight in counter_3.most_common(30)]

    return data


def get_region_case_count_and_top_type_data():
    results = []
    for region in Region.objects.all():
        qs = (
            Case.objects.filter(region=region)
                .values('type__name').order_by()
                .annotate(count=Count('id'))
                .order_by('-count')
        )
        if qs:
            results.append({
                'region_name': region.name,
                'top_type_name': qs.first()['type__name'],
                'case_counts': sum(qs.values_list('count', flat=True))
            })
    qs_all = (
        Case.objects.all()
            .values('type__name').order_by()
            .annotate(count=Count('id'))
            .order_by('-count')
    )
    if qs_all:
        results.append({
            'region_name': '總計',
            'top_type_name': qs_all.first()['type__name'],
            'case_counts': sum(qs_all.values_list('count', flat=True))
        })
    return results
