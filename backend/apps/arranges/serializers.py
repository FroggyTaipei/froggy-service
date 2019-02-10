from rest_framework import serializers
from .models import Arrange


class FilteredPublishedArrangeSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(state='published')
        return super(FilteredPublishedArrangeSerializer, self).to_representation(data)


class ArrangeSerializer(serializers.ModelSerializer):
    arrange_time = serializers.SerializerMethodField()

    def get_arrange_time(self, obj):
        return obj.arrange_time.strftime('%Y-%m-%d')

    class Meta:
        model = Arrange
        list_serializer_class = FilteredPublishedArrangeSerializer
        fields = ('title', 'content', 'arrange_time')
