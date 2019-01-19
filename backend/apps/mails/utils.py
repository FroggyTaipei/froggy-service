import sendgrid
from django.conf import settings
from sendgrid.helpers.mail import Personalization, Content, Mail, Email


def sendgrid_system_mail(message):
    if not settings.USE_SENDGRID:
        raise NotImplementedError('Set USE_SENDGRID to True to use.')

    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)

    from_email = settings.EMAIL_HOST_USER

    subject = "選服系統系統通知"

    message = Content("text/plain", message)

    mail = Mail(from_email, subject, to_email=None, content=message)

    personalization = Personalization()
    for admin, email in settings.ADMINS:
        personalization.add_to(Email(email, admin))
    mail.add_personalization(personalization)

    return sg.client.mail.send.post(request_body=mail.get())
