from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import MarqueeMessageSerializer
from .models import MarqueeMessage


class MarqueeMessageViewSet(ReadOnlyModelViewSet):
    queryset = MarqueeMessage.objects.all()
    serializer_class = MarqueeMessageSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']

    @method_decorator(cache_page(60 * 5))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
