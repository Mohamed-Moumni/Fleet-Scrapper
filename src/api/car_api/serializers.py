from rest_framework import serializers
from .models import Car, Make, Model, SubModel


class MakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = "__all__"


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = "__all__"


class SubModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubModel
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    make = serializers.StringRelatedField()
    sub_model = serializers.StringRelatedField()

    class Meta:
        model = Car
        fields = "__all__"
