import environ

from django.http import JsonResponse, HttpResponse
from django.core.signing import TimestampSigner
from django.utils.translation import ugettext_lazy as _

from suit_dashboard import DashboardView, Grid, Column, Row

from . import boxes

env = environ.Env()


ACCOUNTKIT_APP_ID = env.str('VUE_APP_ACCOUNTKIT_APP_ID')


class DashboardMainView(DashboardView):
    template_name = 'main.html'
    crumbs = ({'url': 'admin:index', 'name': _("Dashboard")},)
    grid = Grid(
        Row(
            Column(boxes.CaseStatePieBox(), width=4),
            Column(boxes.CaseTypeLineBox(), width=4),
            Column(boxes.CaseTypePieBox(), width=4),
        ),
        Row(
            Column(boxes.CaseContentWordCloudBox(), width=4),
            Column(boxes.CaseRegionLineBox(), width=4),
            Column(boxes.CaseRegionPieBox(), width=4),
        ),
    )


def get_token(request):
    signer = TimestampSigner()
    state = signer.sign(ACCOUNTKIT_APP_ID)
    return JsonResponse({
        'state': state,
    })
