from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .api import (
    make_create_api,
    car_get_api,
    model_create_api,
    submodel_create_api,
    car_create_api,
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("make", make_create_api, name="make_create_api"),
    path("search", car_get_api, name="car_get_api"),
    path("model", model_create_api, name="model_create_api"),
    path("submodel", submodel_create_api, name="submodel_create_api"),
    path("car", car_create_api, name="car_create_api"),
]
