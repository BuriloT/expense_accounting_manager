from rest_framework import serializers

from api.models import Category, Transaction, Organization

from users.serializers import User


class CategorySerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)

    class Meta:
        fields = ['name', 'description']
        model = Category


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'description']
        model = Organization


class TransactionSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)

    class Meta:
        fields = ['amount', 'description', 'category', 'organization',
                  'time', 'user']
        read_only_fields = ('time',)
        model = Transaction

    def create(self, validated_data):
        transaction_user = validated_data['user']
        transaction = Transaction.objects.create(**validated_data)
        user = User.objects.filter(id=transaction_user.id).first()
        user.balance += validated_data['amount']
        user.save()
        return transaction

    def update(self, instance, validated_data):
        difference = validated_data['amount'] - instance.amount
        if validated_data['user'] != instance.user:
            instance.user.balance -= instance.amount
            instance.user.save()
            instance.user = validated_data.get('user', instance.user)
            instance.user.balance += validated_data['amount']
        else:
            instance.user.balance += difference
        instance.user.save()
        return super().update(instance, validated_data)
