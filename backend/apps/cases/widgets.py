import json
from suit_dashboard import Widget

from .charts import (
    case_state_pie,
    case_region_pie,
    case_region_line_monthly,
    case_type_pie,
    case_type_line_monthly,
    case_content_wordcloud,
)


class CaseStatePie(Widget):
    html_id = 'case-state-pie-chart'
    template = 'highchart.html'

    @property
    def content(self):
        return json.dumps(case_state_pie())


class CaseRegionPie(Widget):
    html_id = 'case-region-pie-chart'
    template = 'highchart.html'

    @property
    def content(self):
        return json.dumps(case_region_pie())


class CaseTypePie(Widget):
    html_id = 'case-type-pie-chart'
    template = 'highchart.html'

    @property
    def content(self):
        return json.dumps(case_type_pie())


class CaseRegionLineMonthly(Widget):
    html_id = 'case-region-line-monthly-chart'
    template = 'highchart.html'

    @property
    def content(self):
        return json.dumps(case_region_line_monthly())


class CaseTypeLineMonthly(Widget):
    html_id = 'case-type-line-monthly-chart'
    template = 'highchart.html'

    @property
    def content(self):
        return json.dumps(case_type_line_monthly())


class CaseContentWordCloud(Widget):
    html_id = 'case-content-wordcloud'
    template = 'highchart.html'

    @property
    def content(self):
        return json.dumps(case_content_wordcloud())
