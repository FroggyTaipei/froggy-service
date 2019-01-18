from suit_dashboard import Box

from apps.cases.widgets import (
    CaseStatePie,
    CaseRegionPie,
    CaseTypePie,
    CaseTypeLineMonthly,
    CaseRegionLineMonthly,
    CaseContentWordCloud,
)


class CaseStatePieBox(Box):
    title = '現在是處理到哪裡？'
    description = ''
    widgets = [CaseStatePie()]


class CaseRegionPieBox(Box):
    title = '你的使用者多在哪些選區？'
    description = ''
    widgets = [CaseRegionPie()]


class CaseRegionLineBox(Box):
    title = '每個月處理了多少案件（按類別）？'
    description = ''
    widgets = [CaseRegionLineMonthly()]


class CaseTypePieBox(Box):
    title = '你的使用者都在意哪些議題？'
    description = ''
    widgets = [CaseTypePie()]


class CaseTypeLineBox(Box):
    title = '每個月處理了多少案件（按選區）'
    description = ''
    widgets = [CaseTypeLineMonthly()]


class CaseContentWordCloudBox(Box):
    title = '大家到底是在靠北什麼？'
    description = ''
    widgets = [CaseContentWordCloud()]
