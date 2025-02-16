from django.urls import path
from .api import make_create_api, car_get_api

urlpatterns = [
    path("make", make_create_api, name="make_create_api"),
    path("search", car_get_api, name="car_get_api"),
]
