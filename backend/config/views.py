from django.utils.translation import ugettext_lazy as _

from suit_dashboard import DashboardView, Grid, Column, Row

from . import boxes


class DashboardMainView(DashboardView):
    template_name = 'main.html'
    crumbs = ({'url': 'admin:index', 'name': _("Dashboard")},)
    grid = Grid(
        Row(
            Column(boxes.CaseStatePieBox(), width=4),
            Column(boxes.CaseTypePieBox(), width=4),
            Column(boxes.CaseRegionPieBox(), width=4),
        ),
        Row(
            Column(boxes.CaseStatePackedBubbleBox(), width=4),
            Column(boxes.CaseTypePackedBubbleBox(), width=4),
            Column(boxes.CaseRegionPackedBubbleBox(), width=4),
        ),
        Row(
            Column(boxes.CaseContentWordCloudBox(), width=4),
            Column(boxes.CaseTypeLineBox(), width=4),
            Column(boxes.CaseRegionLineBox(), width=4),
        ),
    )
