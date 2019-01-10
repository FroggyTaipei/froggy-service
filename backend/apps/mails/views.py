from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from .models import SendGridMail
from .serializers import SendGridMailSerializer


class MailViewSet(ModelViewSet):
    queryset = SendGridMail.objects.all()
    serializer_class = SendGridMailSerializer

    @action(methods=['GET'], detail=True, permission_classes=[IsAdminUser])
    def resend(self, request, pk=None):
        mail = SendGridMail.objects.get(id=pk)
        mail.send()
        return redirect(reverse("admin:cases_case_change", args=(mail.case.id,)))
