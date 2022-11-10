from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator

from api.models import Category


class User(AbstractUser):
    email = models.EmailField(
        max_length=254, unique=True, blank=False,
        null=False, verbose_name='Email')
    balance = models.FloatField(
        'баланс',
        default=0
    )
    categories = models.ManyToManyField(
        Category,
        through='UserCategory',
        related_name="users",
        verbose_name="категории"
    )

    class Meta:
        ordering = ['username']
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username


class UserCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='user_category'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_category'
    )

    class Meta:
        verbose_name = 'категория пользователя'
        verbose_name_plural = 'категории пользователей'

    def __str__(self):
        return f'{self.category} - {self.user}'
