from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import MakeService, CarService
from .schemas import MakeSchema
from .models import Make
from pydantic import ValidationError
from .serializers import CarSerializer
import json


@api_view(["POST"])
def make_create_api(request):
    try:
        data = MakeSchema(**request.data)
        make_service: MakeService = MakeService(data.name)
        make: Make = make_service.create()
        return Response(
            {
                "message": "Make created successfully",
                "data": json.dumps({"name": make.name}),
            },
            status=status.HTTP_201_CREATED,
        )
    except ValidationError as e:
        return Response({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def car_get_api(request):
    filters = {}
    if "make" in request.GET:
        filters["make__name__iexact"] = request.GET["make"]
    if "model" in request.GET:
        filters["model__name__iexact"] = request.GET["model"]
    if "sub_model" in request.GET:
        filters["sub_model__name__iexact"] = request.GET["sub_model"]
    if "category" in request.GET:
        filters["category__iexact"] = request.GET["category"]
    car_service = CarService()
    cars = car_service.get_by_filter(**filters)
    serializer = CarSerializer(cars, many=True)
    return Response(
        {"message": "cars found successfully", "data": json.dumps(serializer.data)},
        status=status.HTTP_200_OK,
    )
