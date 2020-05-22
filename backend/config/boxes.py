from suit_dashboard import Box

from apps.cases import widgets


class CaseStatePieBox(Box):
    title = '案件狀態百分比'
    description = ''
    widgets = [widgets.CaseStatePie()]


class CaseStatePackedBubbleBox(Box):
    title = '狀態案件數'
    description = ''
    widgets = [widgets.CaseStatePackedBubble()]


class CaseRegionPieBox(Box):
    title = '地區案件百分比'
    description = ''
    widgets = [widgets.CaseRegionPie()]


class CaseRegionPackedBubbleBox(Box):
    title = '地區案件數'
    description = ''
    widgets = [widgets.CaseRegionPackedBubble()]


class CaseRegionLineBox(Box):
    title = '累計案件數（按選區）'
    description = ''
    widgets = [widgets.CaseRegionLine()]


class CaseTypePieBox(Box):
    title = '分類案件百分比'
    description = ''
    widgets = [widgets.CaseTypePie()]


class CaseTypePackedBubbleBox(Box):
    title = '分類案件數'
    description = ''
    widgets = [widgets.CaseTypePackedBubble()]


class CaseTypeLineBox(Box):
    title = '累計案件數（按類別）'
    description = ''
    widgets = [widgets.CaseTypeLine()]


class CaseContentWordCloudBox(Box):
    title = '最常出現的關鍵字'
    description = ''
    widgets = [widgets.CaseContentWordCloud()]
