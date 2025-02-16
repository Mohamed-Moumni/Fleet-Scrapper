from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Make(BaseModel):
    name = models.CharField(unique=True)


class Model(BaseModel):
    name = models.CharField(name="name", unique=True)
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name="models")


class SubModel(BaseModel):
    name = models.CharField(name="name", unique=True)
    model = models.ForeignKey(
        Model, on_delete=models.CASCADE, related_name="sub_models"
    )


class Car(BaseModel):
    name = models.CharField()
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name="cars")
    year = models.IntegerField()
    color = models.CharField()
    category = models.CharField()
    engine_type = models.CharField()
    seats = models.IntegerField(default=0)
    transmission = models.CharField()
    top_speed = models.IntegerField(default=0)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="models")
    sub_model = models.ForeignKey(
        SubModel, on_delete=models.CASCADE, related_name="cars"
    )
