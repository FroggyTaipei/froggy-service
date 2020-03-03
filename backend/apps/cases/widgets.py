import pickle
import json
from functools import partial
from suit_dashboard import Widget
from django_redis import get_redis_connection

from config import charts
from . import insights


cache = get_redis_connection('default')


class InsightWidget(Widget):
    data_func = None
    chart_template = None

    @property
    def content(self):
        cached_data = cache.get(self.data_func.__name__)
        data = pickle.loads(cached_data) if cached_data else self.data_func()
        return json.dumps(self.chart_template(data=data))


class CaseStatePie(InsightWidget):
    html_id = 'case-state-pie-chart'
    template = 'highchart.html'

    data_func = staticmethod(insights.get_case_state_pie_data)
    chart_template = staticmethod(charts.get_highchart_pie)


class CaseRegionPie(InsightWidget):
    html_id = 'case-region-pie-chart'
    template = 'highchart.html'

    data_func = staticmethod(insights.get_case_region_pie_data)
    chart_template = staticmethod(charts.get_highchart_pie)


class CaseTypePie(InsightWidget):
    html_id = 'case-type-pie-chart'
    template = 'highchart.html'

    data_func = staticmethod(insights.get_case_type_pie_data)
    chart_template = staticmethod(charts.get_highchart_pie)


class CaseRegionLineMonthly(InsightWidget):
    html_id = 'case-region-line-monthly-chart'
    template = 'highchart.html'

    data_func = staticmethod(insights.get_case_region_line_monthly_data)
    chart_template = staticmethod(partial(charts.get_highchart_line, y_title='地區'))


class CaseTypeLineMonthly(InsightWidget):
    html_id = 'case-type-line-monthly-chart'
    template = 'highchart.html'

    data_func = staticmethod(insights.get_case_type_line_monthly_data)
    chart_template = staticmethod(partial(charts.get_highchart_line, y_title='案件類型'))


class CaseContentWordCloud(InsightWidget):
    html_id = 'case-content-wordcloud'
    template = 'highchart.html'

    data_func = staticmethod(insights.get_case_content_wordcloud_data)
    chart_template = staticmethod(charts.get_highchart_word_cloud)
