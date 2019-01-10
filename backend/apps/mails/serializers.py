from rest_framework import serializers
from apps.mails.models import SendGridMail


class SendGridMailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SendGridMail
        fields = '__all__'
