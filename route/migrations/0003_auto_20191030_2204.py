# Generated by Django 2.1.5 on 2019-10-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0002_station_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='routes',
            field=models.ManyToManyField(related_name='stations', to='route.Route'),
        ),
    ]