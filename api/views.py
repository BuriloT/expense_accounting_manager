from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from api.models import Category, Transaction, Organization
from api.serializers import (CategorySerializer, OrganizationSerializer,
                             TransactionSerializer)
from api.filters import SearchFilterBackend


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [filters.OrderingFilter, SearchFilterBackend]
    ordering_fields = ['amount', 'time']
    search_fields = ['amount', 'time']

    def destroy(self, request, pk):
        transaction = self.get_object()
        transaction.user.balance -= transaction.amount
        transaction.user.save()
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
