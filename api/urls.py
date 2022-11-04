from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import CategoryViewSet

router_v1 = DefaultRouter()
router_v1.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
]
