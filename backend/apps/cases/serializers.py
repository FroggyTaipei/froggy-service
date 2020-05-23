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
    region = serializers.SerializerMethodField(read_only=True)
    state = serializers.SerializerMethodField(read_only=True)

    def get_create_time(self, obj):
        return obj.create_time.strftime('%Y-%m-%d')

    def get_type(self, obj):
        return obj.type.name

    def get_region(self, obj):
        return obj.region.name

    def get_state(self, obj):
        return obj.state_title

    class Meta:
        model = Case
        fields = ['id', 'number', 'create_time', 'title', 'content', 'location', 'type', 'state', 'region']


class CaseRetrieveSerializer(CaseSerializer):
    arranges = ArrangeSerializer(many=True)

    class Meta:
        model = Case
        fields = ['id', 'number', 'create_time', 'title',
                  'content', 'location', 'type', 'state',
                  'region', 'arranges', 'disapprove_info']


class VuetableParamsExpectations(serializers.Serializer):
    page = serializers.IntegerField(min_value=1, default=1)
    limit = serializers.IntegerField(min_value=1, default=10)
    ascending = serializers.ChoiceField(choices=('desc', 'asc'), default='desc')
    sort = serializers.ChoiceField(choices=('id', 'state', 'type', 'create_time'), default='id')
    query = serializers.CharField(required=False)
    type = serializers.IntegerField(required=False)
    state = serializers.ChoiceField(required=False, choices=('disapproved', 'arranged', 'closed'))
