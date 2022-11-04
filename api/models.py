from django.db import models


class Category(models.Model):
    name = models.CharField(
        'название',
        max_length=128,
        unique=True
    )
    description = models.CharField(
        'описание',
        max_length=256
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
        max_length=256
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
    time = models.DateField(
        'Время'
    )
    categories = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='transaction',
        verbose_name='категории'
    )
    organizations = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='transaction',
        verbose_name='организации'
    )
    description = models.CharField(
        'описание',
        max_length=256
    )

    class Meta:
        verbose_name = 'транзакция'
        verbose_name_plural = 'транзацкции'

    def __str__(self):
        return f'{self.amount} - {self.time} - {self.description}'
