from django.urls import path
from . import views

app_name = 'route'

urlpatterns = [
    path('stations/', views.route_view, name='route'),
]