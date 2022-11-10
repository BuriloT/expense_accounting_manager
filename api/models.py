from datetime import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(
        'название',
        max_length=128,
        unique=True
    )
    description = models.CharField(
        'описание',
        max_length=256,
        blank=True
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name[:50]


class Organization(models.Model):
    name = models.CharField(
        'название',
        max_length=128
    )
    description = models.CharField(
        'описание',
        max_length=256,
        blank=True
    )

    class Meta:
        verbose_name = 'организация'
        verbose_name_plural = 'организации'

    def __str__(self):
        return self.name[:50]


class Transaction(models.Model):
    amount = models.FloatField(
        'сумма',
    )
    time = models.DateTimeField(
        'Время',
        default=datetime.now().strftime(("%Y-%m-%d %H:%M:%S.%f")),
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='transaction',
        verbose_name='категории'
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='transaction',
        verbose_name='организации'
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='transaction',
        verbose_name='пользователи'
    )
    description = models.CharField(
        'описание',
        max_length=256,
        blank=True
    )

    class Meta:
        verbose_name = 'транзакция'
        verbose_name_plural = 'транзацкции'

    def __str__(self):
        return f'{self.amount} - {self.time} - {self.description}'
