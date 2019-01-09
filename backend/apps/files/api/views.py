from rest_framework import viewsets, status
from rest_framework.decorators import action, list_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.cases.models import Case
from apps.files import models

from . import serializers


class TempFileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TempFileSerializer
    queryset = models.TempFile.objects.all()

    def perform_create(self, serializer):
        try:
            return Response('test')
            super(TempFileViewSet, self).perform_create(serializer)
        except Exception as e:
            return Response(str(e))

    # def create(self, request, *args, **kwargs):
    #     try:
    #         return super(TempFileViewSet, self).create(request, *args, **kwargs)
    #     except Exception as e:
    #         return Response(str(e))

    @action(methods=['GET'], detail=True)
    def all(self, request, pk=None):
        queryset = self.queryset.filter(case=pk)
        serializer = self.get_serializer(queryset, many=True)

        if len(serializer.data) > 0:
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CaseFileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CaseFileSerializer
    queryset = models.CaseFile.objects.all()
    permission_classes = []

    @action(methods=['GET'], detail=True)
    def all(self, request, pk=None):
        case = Case.objects.filter(number=pk)
        queryset = self.queryset.filter(case__in=case)
        serializer = self.get_serializer(queryset, many=True)

        if len(serializer.data) > 0:
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
