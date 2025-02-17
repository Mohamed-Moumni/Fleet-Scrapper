from django.db import transaction, IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from typing import List
from .models import Car, Make, Model, SubModel


class MakeService:
    def __init__(self):
        pass

    @staticmethod
    def create(name: str):
        new_make, created = Make.objects.get_or_create(name=name)
        return new_make

    def get(name: str):
        make = Make.objects.get(name=name)
        return make


class ModelService:
    def __init__(self):
        pass

    @staticmethod
    def create(**kwargs):
        new_model = Model.objects.filter(name=kwargs.get("name")).first()

        if new_model is None:
            make_id = kwargs.get("make_id")
            if not Make.objects.filter(id=int(make_id)).exists():
                raise ValueError(f"Make with id {make_id} does not exist.")

            new_model = Model.objects.create(**kwargs)
        return new_model

    @staticmethod
    def get(name: str):
        model = Model.objects.get(name=name)
        return model


class SubModelService:
    def __init__(self):
        pass

    @staticmethod
    def create(**kwargs):
        new_sub_model = SubModel.objects.filter(name=kwargs.get("name")).first()

        if new_sub_model is None:
            sub_model_id = kwargs.get("sub_model_id")
            if not SubModel.objects.filter(id=int(sub_model_id)).exists():
                raise ValueError(f"Make with id {sub_model_id} does not exist.")

            new_sub_model = SubModel.objects.create(**kwargs)
        return new_sub_model

    @staticmethod
    def get(name: str):
        sub_model = SubModel.objects.get(name=name)
        return sub_model


class CarService:
    def __init__(self):
        pass

    @transaction.atomic
    @staticmethod
    def create(**kwargs):
        try:
            make = Make.objects.get(id=kwargs.get("make_id"))
            model = Model.objects.get(id=kwargs.get("model_id"))
            sub_model = SubModel.objects.get(id=kwargs.get("sub_model_id"))

            car = Car.objects.create(
                make=make, model=model, sub_model=sub_model, **kwargs
            )
            return car
        except ObjectDoesNotExist:
            raise ValueError("One or more related objects do not exist.")
        except Exception as e:
            raise ValueError(f"An error occurred while creating the car. {e}")

    def get_by_filter(self, **filters):
        cars_filtered: List[Car] = Car.objects.filter(**filters)
        return cars_filtered
