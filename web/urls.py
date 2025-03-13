from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('home/', views.index, name='index'),
    # returns JSON of allowed resevation tims
    path('api/get_times', views.get_times, name='get_times'),
    # make reservation
    path('api/reserve', views.reserve, name="make_reservation"),
]
