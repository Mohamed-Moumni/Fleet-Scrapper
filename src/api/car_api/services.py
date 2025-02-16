from django.db import transaction
from typing import List
from .models import Car, Make, Model, SubModel


class MakeService:
    def __init__(self):
        pass

    @staticmethod
    def create(name: str):
        new_make, created = Make.objects.get_or_create(name=name)
        return new_make


class ModelService:
    def __init__(self):
        pass

    @staticmethod
    def create(**kwargs):
        new_model, created = Model.objects.get_or_create(**kwargs)
        return new_model


class SubModelService:
    def __init__(self):
        pass

    @staticmethod
    def create(**kwargs):
        new_sub_model, created = SubModel.objects.get_or_create(**kwargs)
        return new_sub_model


class CarService:
    def __init__(self):
        pass

    @transaction.atomic
    def create(self, **kwargs):
        new_car, created = Car.objects.get_or_create(**kwargs)
        return new_car

    def get_by_filter(self, **filters):
        cars_filtered: List[Car] = Car.objects.filter(**filters)
        return cars_filtered
