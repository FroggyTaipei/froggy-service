from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.files import models
from apps.users.authentication import AccountKitUserAuthentication

from . import serializers


class TempFileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TempFileSerializer
    queryset = models.TempFile.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [AccountKitUserAuthentication]
    http_method_names = ['post', 'delete']

    def perform_create(self, serializer):
        user = self.request.user
        serializer.validated_data['user'] = user
        serializer.save()
