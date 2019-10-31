from django.shortcuts import render
from route.models import Route


def route_view(request):
    template = 'stations.html'
    routes = Route.objects.all().prefetch_related('stations')
    stations = None

    route = request.GET.get('route')
    if route:
        stations = routes.get(name=route).stations.all()

    stations_latitude = stations.order_by('latitude')
    stations_longitude = stations.order_by('longitude')
    x = (stations_latitude[0].latitude + stations_latitude[len(stations_latitude)-1].latitude) / 2
    y = (stations_longitude[0].longitude + stations_longitude[len(stations_longitude) - 1].longitude) / 2
    center = {
        'x': x,
        'y': y,
    }

    context = {
        'routes': routes,
        'stations': stations,
        'route': route,
        'center': center
    }

    return render(request, template, context)
