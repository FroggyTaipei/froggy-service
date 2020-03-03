from rest_framework import serializers
from .models import MarqueeMessage


class MarqueeMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MarqueeMessage
        fields = ('message', 'order', 'display')
