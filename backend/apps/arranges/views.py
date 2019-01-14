from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import ArrangeSerializer
from .models import Arrange


class ArrangeViewSet(ReadOnlyModelViewSet):
    queryset = Arrange.objects.all()
    serializer_class = ArrangeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get']
