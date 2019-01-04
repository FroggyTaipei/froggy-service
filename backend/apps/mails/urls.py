from django.urls import path
from .views import resend_email_view


app_name = 'mails'

urlpatterns = [
    path('resend-email/<int:id>/', resend_email_view, name='resend-email'),
]
