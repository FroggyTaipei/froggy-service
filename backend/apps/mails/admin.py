from django.contrib import admin
from .models import SendGridMail, SendGridMailTemplate


admin.site.register(SendGridMailTemplate)
admin.site.register(SendGridMail)
