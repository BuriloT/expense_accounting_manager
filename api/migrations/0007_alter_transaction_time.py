# Generated by Django 4.1.3 on 2022-11-10 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_transaction_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(blank=True, default='2022-11-10 09:57:10.863617', verbose_name='Время'),
        ),
    ]