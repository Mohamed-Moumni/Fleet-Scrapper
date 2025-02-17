from django.test import TestCase
from .services import MakeService, ModelService, SubModelService, CarService


class TestModelService(TestCase):
    def test_model_service(self):
        make_service = MakeService()
        model_service = ModelService()

        make = make_service.create("Dacia")
        data = {"name": "Dacia Duster", "make": make}
        model = model_service.create(**data)

        self.assertEqual(model.name, "Dacia Duster")


class TestSubModelService(TestCase):
    def setUp(self):
        make_service = MakeService()
        model_service = ModelService()

        make = make_service.create("Dacia")
        model_data = {"name": "Dacia Duster", "make": make}
        model = model_service.create(**model_data)
        self.model = model

    def test_sub_model_service(self):
        self.setUp()
        sub_model_service = SubModelService()

        sub_model_data = {"name": "dacia-gen-01", "model": self.model}
        sub_model = sub_model_service.create(**sub_model_data)
        self.assertEqual(sub_model.name, "dacia-gen-01")


class TestCarService(TestCase):
    def setUp(self):
        make_service = MakeService()
        model_service = ModelService()
        sub_model_service = SubModelService()

        make = make_service.create("Dacia")
        model_data = {"name": "Dacia Duster", "make": make}
        model = model_service.create(**model_data)
        sub_model_data = {"name": "dacia-gen-01", "model": model}
        sub_model = sub_model_service.create(**sub_model_data)
        print(make, model, sub_model)
        self.model = model
        self.sub_model = sub_model
        self.make = make

    def test_car_service(self):
        self.setUp()
        car_service = CarService()
        car_data = {
            "name": "Dacia Logan",
            "make": self.make,
            "year": "2020",
            "color": "#ffff",
            "category": "Luxury",
            "engine_type": "Fuel",
            "seats": 4,
            "transmission": "manual",
            "top_speed": 120,
            "model": self.model,
            "sub_model": self.sub_model,
        }
        car = car_service.create(**car_data)
        self.assertEqual(car.name, "Dacia Logan")
