from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services import MakeService, CarService, ModelService, SubModelService
from .schemas import MakeSchema, ModelSchema, SubModelSchema, CarSchema
from .models import Make, Model, SubModel, Car
from pydantic import ValidationError
from .serializers import CarSerializer
import json



@api_view(["POST"])
def make_create_api(request):
    try:
        data = MakeSchema(**request.data)
        make: Make = MakeService.create(data.name)
        return Response(
            {
                "message": "Make created successfully",
                "data": json.dumps({"name": make.name, "id": make.id}),
            },
            status=status.HTTP_201_CREATED,
        )
    except ValidationError as e:
        return Response({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def model_create_api(request):
    try:
        data = ModelSchema(**request.data)
        model: Model = ModelService.create(**data.dict())
        return Response(
            {
                "message": "Model created successfully",
                "data": json.dumps({"name": model.name, "id": model.id}),
            }
        )
    except ValidationError as e:
        return Response({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)


# create sub_model

@api_view(["POST"])
def submodel_create_api(request):
    try:
        data = SubModelSchema(**request.data)
        submodel: SubModel = SubModelService.create(**data.dict())
        return Response(
            {
                "message": "Submodel created successfully",
                "data": json.dumps({"name": submodel.name, "id": submodel.id}),
            }
        )
    except ValidationError as e:
        return Response({"errors": e.errors()}, status=status.HTTP_400_BAD_REQUEST)

# create car

@api_view(["POST"])
def car_create_api(request):
    try:
        data = CarSchema(**request.data)
        car: Car = CarService.create(**data.dict())
        return Response(
            {
                "message": "Car created successfully",
                "data": json.dumps({"name": car.name, "id": car.id}),
            }
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
