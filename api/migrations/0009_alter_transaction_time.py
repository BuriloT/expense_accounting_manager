# Generated by Django 4.1.3 on 2022-11-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(blank=True, default='2022-11-10 10:44:52.616367', verbose_name='Время'),
        ),
    ]