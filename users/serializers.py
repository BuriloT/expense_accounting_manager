from django.forms import ValidationError
from rest_framework import serializers

from users.models import User, UserCategory
from api.models import Category
from api.serializers import CategorySerializer


class UserCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCategory
        fields = ['category', 'user']


class UserSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'balance', 'categories']


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    balance = serializers.FloatField(read_only=True, required=False, default=0)
    categories = serializers.CharField(required=False, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'balance', 'categories']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["categories"] = CategorySerializer(
            instance.categories.all(), many=True
        ).data
        return rep

    def create(self, validated_data):
        categories = Category.objects.all()[:11]
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.categories.set(categories)
        user.save()
        return user

    def validate_password(self, data):
        password = data
        if len(password) < 5:
            return ValidationError('Пароль не должен быть меньше 4 символов!')
        return password
