from django.db import models


class Station(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    routes = models.ManyToManyField('Route', related_name='stations')
    name = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
