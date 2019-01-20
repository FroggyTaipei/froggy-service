from rest_framework import serializers
from apps.arranges.serializers import ArrangeSerializer
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


class CaseWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Case
        fields = ['uuid', 'title', 'content', 'location', 'username', 'email', 'address', 'type', 'region']


class CaseSerializer(serializers.ModelSerializer):
    create_time = serializers.SerializerMethodField(read_only=True)
    type = serializers.SerializerMethodField(read_only=True)
    state = serializers.SerializerMethodField(read_only=True)

    def get_create_time(self, obj):
        return obj.create_time.strftime('%Y-%m-%d')

    def get_type(self, obj):
        return obj.type.name

    def get_state(self, obj):
        return obj.state_title

    class Meta:
        model = Case
        fields = ['id', 'number', 'create_time', 'title', 'content', 'location', 'type', 'state']


class CaseRetrieveSerializer(CaseSerializer):
    arranges = ArrangeSerializer(many=True)

    class Meta:
        model = Case
        fields = ['id', 'number', 'create_time', 'title',
                  'content', 'location', 'type', 'state',
                  'arranges', 'disapprove_info']
