from django.db import transaction
from typing import List
from .models import Car, Make, Model, SubModel


class MakeService:
    def __init__(self, name: str):
        self.name = name

    def create(self):
        new_make: Make = Make.objects.create(name=self.name)
        return new_make


class ModelService:
    def __init__(self):
        pass

    def create(self, name: str):
        new_model: Model = Model.objects.create(name)
        return new_model


class SubModelService:
    def __init__(self):
        pass

    def create(self, **kwargs):
        new_sub_model: SubModel = SubModel.objects.create(**kwargs)
        return new_sub_model


class CarService:
    def __init__(self):
        pass

    @transaction.atomic
    def create(self, **kwargs):
        new_car: Car = Car.objects.create(**kwargs)
        return new_car

    def get_by_filter(self, **filters):
        cars_filtered: List[Car] = Car.objects.filter(**filters)
        return cars_filtered
