import pytest
from django.test import TestCase
from .services import MakeService
from .models import Make
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class TestMakeService(TestCase):
    def setUp(self):
        self.make_service = MakeService(name="Test Make Service")

    def test_create_make_success(self):
        make_data = {"name": "Toyota"}

        make = self.make_service.create(**make_data)

        assert make.name == make_data["name"]
        assert Make.objects.count() == 1

    def test_create_make_without_name(self):
        make_data = {}

        with pytest.raises(ValidationError):
            self.make_service.create(**make_data)
