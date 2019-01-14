from rest_framework import serializers
from .models import Arrange


class ArrangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Arrange
        fields = ('title', 'content', 'arrange_time')
