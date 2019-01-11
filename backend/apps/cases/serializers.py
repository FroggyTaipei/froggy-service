from rest_framework import serializers
from .models import (
    Type,
    Region,
    Case,
)


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = '__all__'
