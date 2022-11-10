from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import CategoryViewSet, OrganizationViewSet, TransactionViewSet

router_v1 = DefaultRouter()
router_v1.register('category', CategoryViewSet)
router_v1.register('organization', OrganizationViewSet)
router_v1.register('transaction', TransactionViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
]
