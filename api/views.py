from rest_framework import viewsets

from api.models import Category, Transaction, Organization
from api.serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
