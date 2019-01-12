from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.files import models

from . import serializers


class TempFileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TempFileSerializer
    queryset = models.TempFile.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['post', 'delete']
