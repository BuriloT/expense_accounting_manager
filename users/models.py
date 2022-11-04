from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.validators import RegexValidator

from api.models import Category


class User(AbstractUser):
    # username = models.CharField(
    #     max_length=150, validators=[RegexValidator[r"^[\w.@+-]+\Z"]],
    #     unique=True, verbose_name='Имя пользователя')
    email = models.EmailField(
        max_length=254, unique=True, blank=False,
        null=False, verbose_name='Email')
    balance = models.FloatField(
        'баланс',
        default=0
    )
    categories = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="users",
        verbose_name="категории"
    )

    class Meta:
        ordering = ['username']
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username
