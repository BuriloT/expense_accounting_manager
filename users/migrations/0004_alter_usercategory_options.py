# Generated by Django 4.1.3 on 2022-11-09 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_categories_usercategory_user_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercategory',
            options={'verbose_name': 'категория пользователя', 'verbose_name_plural': 'категории пользователей'},
        ),
    ]
