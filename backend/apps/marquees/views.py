from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import MarqueeMessageSerializer
from .models import MarqueeMessage


class MarqueeMessageViewSet(ReadOnlyModelViewSet):
    queryset = MarqueeMessage.objects.all()
    serializer_class = MarqueeMessageSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']
