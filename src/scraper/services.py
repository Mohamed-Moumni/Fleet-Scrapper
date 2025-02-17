from dotenv import load_dotenv
from pathlib import Path
import json
from os import getenv
from pydantic import ValidationError
import requests

load_dotenv(dotenv_path=Path("../.env"))


class Service:
    def __init__(self):
        self.server_host = getenv("DJANGO_HOST")
        self.server_port = getenv("DJANGO_PORT")

    def create_make(self, name: str):
        try:
            data = {"name": name}
            response = requests.post(
                f"{self.server_host}:{self.server_port}/api/make", json=data
            ).json()
            response = json.loads(response["data"])
            return response["id"]
        except ValidationError as e:
            return None

    def create_model(self, **kwargs):
        try:
            response = requests.post(
                f"{self.server_host}:{self.server_port}/api/model", json=kwargs
            ).json()
            response = json.loads(response["data"])
            return response["id"]
        except ValidationError as e:
            return None

    def create_submodel(self, **kwargs):
        try:
            response = requests.post(f"{self.server_host}:{self.server_port}/api/submodel", json=kwargs).json()
            response = json.loads(response["data"])
            return response["id"]
        except ValidationError as e:
            return None

    def create_car(self, **kwargs):
        try:
            response = requests.post(f"{self.server_host}:{self.server_port}/api/car", json=kwargs).json()
            print(f"Response: {response}")
            response = json.loads(response["data"])
            return response["id"]
        except ValidationError as e:
            return None
