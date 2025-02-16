import os
import sys
import django
from pathlib import Path


def setup_django():
    current_dir = Path(__file__).resolve().parent
    project_root = current_dir.parent
    api_path = project_root / "api"

    sys.path.append(str(project_root))
    sys.path.append(str(api_path))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

    django.setup()


def get_car_service():
    try:
        from car_api.services import CarService

        return CarService()
    except ImportError as e:
        raise ImportError(f"Failed to import CarService: {str(e)}")


def get_model_service():
    try:
        from car_api.services import ModelService

        return ModelService()
    except ImportError as e:
        raise ImportError(f"Failed to import CarService: {str(e)}")


def get_sub_model_service():
    try:
        from car_api.services import SubModelService

        return SubModelService()
    except ImportError as e:
        raise ImportError(f"Failed to import CarService: {str(e)}")


def get_make_service():
    try:
        from car_api.services import MakeService

        return MakeService()
    except ImportError as e:
        raise ImportError(f"Failed to import CarService: {str(e)}")
