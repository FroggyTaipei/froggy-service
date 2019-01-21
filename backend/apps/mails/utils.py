from django.conf import settings
from django.core.mail import send_mail


def sendgrid_system_mail(message):
    from_email = settings.SERVER_EMAIL

    subject = "選服系統系統通知"

    admins = [email for name, email in settings.ADMINS]

    return send_mail(subject, message, from_email, admins, fail_silently=False)
