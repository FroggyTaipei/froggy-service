import pickle
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from django_redis import get_redis_connection

from apps.users.authentication import AccountKitUserAuthentication
from apps.arranges.models import Arrange
from .serializers import (
    CaseWriteSerializer,
    CaseSerializer,
    CaseRetrieveSerializer,
    TypeSerializer,
    RegionSerializer,
    VuetableParamsExpectations,
)
from .models import (
    Type,
    Region,
    Case,
)
from .schemas import vuetable_schema
from . import insights


class RegionViewSet(ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = []
    http_method_names = ['get']

    @method_decorator(cache_page(60 * 60 * 24 * 14))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class TypeViewSet(ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = []
    http_method_names = ['get']

    @method_decorator(cache_page(60 * 60 * 24 * 14))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CaseViewSet(ModelViewSet):
    queryset = Case.objects.exclude(state='draft')
    serializer_class = CaseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post', 'retrieve']
    pagination_class = LimitOffsetPagination
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('id', 'number', 'type__name', 'location', 'title', 'content',
                     'disapprove_info', 'arranges__title', 'arranges__content')
    ordering_fields = ('id', 'number', 'type')

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return CaseWriteSerializer
        if self.action == 'retrieve':
            return CaseRetrieveSerializer
        return CaseSerializer

    def get_authenticators(self):
        if self.request.method == "POST":
            self.authentication_classes = [AccountKitUserAuthentication]
        return [auth() for auth in self.authentication_classes]

    def perform_create(self, serializer):
        """Create時透過jwt user token，從user instance取得mobile"""
        user = self.request.user
        serializer.validated_data['mobile'] = user.mobile
        serializer.save()

    @action(methods=['GET'], detail=False, schema=vuetable_schema)
    def vuetable(self, request):
        queryset = self.queryset

        qpe = VuetableParamsExpectations(data=request.query_params)
        if not qpe.is_valid():
            return Response(
                data=qpe.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        ascending = qpe.validated_data['ascending']
        sort = qpe.validated_data['sort']
        page = qpe.validated_data['page'] - 1
        limit = qpe.validated_data['limit']
        query = qpe.validated_data.get('query')
        state = qpe.validated_data.get('state')
        _type = qpe.validated_data.get('type')

        if ascending == 'desc':
            sort = '-' + sort

        if query:
            arrange_ids = Arrange.objects.filter(Q(title__icontains=query)
                                                 | Q(content__icontains=query)).values_list('id', flat=True)

            queryset = queryset.filter(Q(number__icontains=query)
                                       | Q(title__icontains=query)
                                       | Q(content__icontains=query)
                                       | Q(location__icontains=query)
                                       | Q(disapprove_info__icontains=query)
                                       | Q(arranges__id__in=arrange_ids)).distinct()

        if state:
            queryset = queryset.filter(state=state)

        if _type:
            queryset = queryset.filter(type__id=_type)

        count = queryset.count()
        start = limit * page
        queryset = queryset.order_by(sort)[start:start+limit]

        serializer = self.serializer_class(queryset, many=True)
        result = {
            'data': serializer.data,
            'count': count,
        }
        return Response(result, status=status.HTTP_200_OK)


class CaseInsightViewSet(ViewSet):
    http_method_names = ['get']
    permission_classes = [AllowAny]

    @staticmethod
    def get_data_from_cache(func):
        cache = get_redis_connection('default')
        cached_data = cache.get(func.__name__)
        return pickle.loads(cached_data) if cached_data else func()

    @action(methods=['GET'], detail=False)
    def case_type_pie(self, request):
        return Response(self.get_data_from_cache(insights.get_case_type_pie_data))

    @action(methods=['GET'], detail=False)
    def case_state_pie(self, request):
        return Response(self.get_data_from_cache(insights.get_case_state_pie_data))

    @action(methods=['GET'], detail=False)
    def case_region_pie(self, request):
        return Response(self.get_data_from_cache(insights.get_case_region_pie_data))

    @action(methods=['GET'], detail=False)
    def case_type_line_monthly(self, request):
        return Response(self.get_data_from_cache(insights.get_case_type_line_monthly_data))

    @action(methods=['GET'], detail=False)
    def case_region_line_monthly(self, request):
        return Response(self.get_data_from_cache(insights.get_case_region_line_monthly_data))

    @action(methods=['GET'], detail=False)
    def case_content_wordcloud(self, request):
        return Response(self.get_data_from_cache(insights.get_case_content_wordcloud_data))
