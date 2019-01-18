from django.db.models import Q
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.users.authentication import AccountKitUserAuthentication
from .serializers import (
    CaseWriteSerializer,
    CaseSerializer,
    CaseRetrieveSerializer,
    TypeSerializer,
    RegionSerializer,
)
from .models import (
    Type,
    Region,
    Case,
)


class RegionViewSet(ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = []
    http_method_names = ['get']


class TypeViewSet(ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = []
    http_method_names = ['get']


class CaseViewSet(ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    http_method_names = ['get', 'post']

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
        case = serializer.save()
        user = self.request.user
        case.mobile = user.mobile
        case.save()

    @action(methods=['GET'], detail=False)
    def vuetable(self, request):
        queryset = self.queryset
        count = self.queryset.count()
        kwargs = self.request.query_params

        limit = int(kwargs.get('limit', None) or 5)
        # by_column = int(kwargs.get('byColumn', None) or 0)
        page = int(kwargs.get('page', None) or 1) - 1
        ascending = kwargs.get('ascending', None) or 'desc'
        query = kwargs.get('query', None) or ''
        order_by = kwargs.get('orderBy', None) or 'id'

        if ascending == 'desc':
            order_by = '-' + order_by

        if query:
            queryset = queryset.filter(Q(number__icontains=query)
                                       | Q(title__icontains=query)
                                       | Q(content__icontains=query)
                                       | Q(location__icontains=query))

        start = limit * page
        queryset = queryset.order_by(order_by)[start:start+limit]

        serializer = self.serializer_class(queryset, many=True)
        result = {
            'data': serializer.data,
            'count': count,
        }
        return Response(result, status=status.HTTP_200_OK)
