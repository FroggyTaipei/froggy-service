from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import SendGridMail


@login_required
def resend_email_view(request, id):
    mail = SendGridMail.objects.get(id=id)
    mail.send()
    return redirect(reverse("admin:cases_case_change", args=(mail.case.id,)))
