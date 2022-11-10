from rest_framework import filters


class SearchFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        if request.query_params.get('amount'):
            return queryset.filter(amount=request.query_params.get('amount'))
        if request.query_params.get('time'):
            return queryset.filter(time=request.query_params.get('time'))
        return queryset
