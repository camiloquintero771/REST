# Generated by Django 3.1.3 on 2023-07-07 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230707_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefono'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefono'),
        ),
    ]
