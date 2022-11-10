from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import (UserViewSet, UserCategoryViewset,
                         CreateRegistration)

router_v1 = DefaultRouter()
router_v1.register('signup', CreateRegistration, basename='signup')
router_v1.register('user', UserViewSet)
router_v1.register(
    r'^users/categories',
    UserCategoryViewset,
    basename='user_category')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
