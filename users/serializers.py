from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    balance = serializers.FloatField(read_only=True, required=False, default=0)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'balance']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
