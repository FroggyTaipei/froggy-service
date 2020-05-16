from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from rest_framework.filters import BaseFilterBackend
from rest_framework.compat import (
    coreapi, coreschema
)


class ExcludeIDFilter(BaseFilterBackend):
    param = 'ids'
    title = _('Exclude by ID.')
    description = _('IDs to exclude.')

    def filter_queryset(self, request, queryset, view):
        terms = self.get_terms(request)
        if not terms:
            return queryset
        return queryset.exclude(id__in=terms)

    def get_terms(self, request):
        """
        Search terms are set by a ?ids=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        params = request.query_params.get(self.param, '')
        return params.replace(',', ' ').split()

    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
        return [
            coreapi.Field(
                name=self.param,
                required=False,
                location='query',
                schema=coreschema.String(
                    title=force_text(self.title),
                    description=force_text(self.description)
                )
            )
        ]


class CaseTypeFilter(BaseFilterBackend):
    param = 'type'
    title = _('Case type.')
    description = _('Filter by type name or ID.')

    def filter_queryset(self, request, queryset, view):
        terms = self.get_terms(request)
        if not terms:
            return queryset
        if terms.isnumeric():
            return queryset.filter(type__id=terms)
        return queryset.filter(type__name=terms)

    def get_terms(self, request):
        """
        Search terms are set by a ?type=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        param = request.query_params.get(self.param, '')
        return param.strip()

    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
        return [
            coreapi.Field(
                name=self.param,
                required=False,
                location='query',
                schema=coreschema.String(
                    title=force_text(self.title),
                    description=force_text(self.description)
                )
            )
        ]


class CaseRegionFilter(BaseFilterBackend):
    param = 'region'
    title = _('Case region.')
    description = _('Filter by region name or ID.')

    def filter_queryset(self, request, queryset, view):
        terms = self.get_terms(request)
        if not terms:
            return queryset
        if terms.isnumeric():
            return queryset.filter(region__id=terms)
        return queryset.filter(region__name=terms)

    def get_terms(self, request):
        """
        Search terms are set by a ?type=... query parameter,
        and may be comma and/or whitespace delimited.
        """
        param = request.query_params.get(self.param, '')
        return param.strip()

    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
        return [
            coreapi.Field(
                name=self.param,
                required=False,
                location='query',
                schema=coreschema.String(
                    title=force_text(self.title),
                    description=force_text(self.description)
                )
            )
        ]
