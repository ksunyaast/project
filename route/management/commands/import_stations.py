import csv

from django.core.management.base import BaseCommand
from route.models import Station, Route


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('moscow_bus_stations.csv', 'r') as csvfile:

            station_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(station_reader)
            routes = Route.objects.all()
            for line in station_reader:
                # TODO: Добавьте сохранение модели
                station = Station(id=line[0], name=line[1], longitude=line[2], latitude=line[3])
                station.save()

                route_numbers = line[7].split('; ')
                for route_number in route_numbers:
                    if routes.filter(name=route_number).exists():
                        station.routes.add(routes.filter(name=route_number)[0])
                    else:
                        route = Route.objects.create(name=route_number)
                        station.routes.add(route)
