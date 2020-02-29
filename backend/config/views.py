from django.utils.translation import ugettext_lazy as _

from suit_dashboard import DashboardView, Grid, Column, Row

from . import boxes


class DashboardMainView(DashboardView):
    template_name = 'main.html'
    crumbs = ({'url': 'admin:index', 'name': _("Dashboard")},)
    grid = Grid(
        Row(
            Column(boxes.CaseStatePieBox(), width=4),
            Column(boxes.CaseContentWordCloudBox(), width=8),
        ),
        Row(
            Column(boxes.CaseTypePieBox(), width=4),
            Column(boxes.CaseTypeLineBox(), width=8),
        ),
        Row(
            Column(boxes.CaseRegionPieBox(), width=4),
            Column(boxes.CaseRegionLineBox(), width=8),
        ),
    )
