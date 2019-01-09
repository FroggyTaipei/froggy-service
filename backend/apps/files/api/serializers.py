from rest_framework import serializers
from apps.files import models


class TempFileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    def get_url(self, obj):
        return obj.url

    class Meta:
        model = models.TempFile
        fields = '__all__'


class CaseFileSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    def get_url(self, obj):
        return obj.url

    class Meta:
        model = models.CaseFile
        fields = '__all__'
