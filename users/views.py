from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import action

from users.models import User, UserCategory
from users.serializers import (UserSerializer, RegistrationSerializer,
                               UserCategorySerializer)


class UserCategoryViewset(viewsets.ModelViewSet):
    queryset = UserCategory.objects.all()
    serializer_class = UserCategorySerializer

    @action(methods=["DELETE"], detail=False)
    def delete(self, request):
        user_category = self.queryset.filter(**request.data)
        user_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateRegistration(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
