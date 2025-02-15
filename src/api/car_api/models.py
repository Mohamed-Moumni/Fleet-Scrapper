from django.db import models


class Car(models.Model):
    name = models.CharField()
    make = models.CharField()
    year = models.IntegerField()
    color = models.CharField()
    category = models.CharField()
    engine_type = models.CharField()
    seats = models.IntegerField(default=0)
    transmission = models.CharField()
    top_speed = models.IntegerField(default=0)


class SubModel(models.Model):
    name = models.CharField(name="Sub Model")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="cars")


class Model(models.Model):
    name = models.CharField(name="Model")
    sub_model = models.ForeignKey(
        SubModel, on_delete=models.CASCADE, related_name="sub_models"
    )


class Make(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="models")
