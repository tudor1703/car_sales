# Generated by Django 4.2.5 on 2025-01-28 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_alter_car_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
