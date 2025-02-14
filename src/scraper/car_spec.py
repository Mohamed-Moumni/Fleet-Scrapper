from bs4 import BeautifulSoup
from requests import Session
from typing import Dict


class Car:
    def __init__(self, **attrs):
        self.name: str = attrs.get("name", "null")
        self.make: str = attrs.get("make", "null")
        self.model: str = attrs.get("model", "null")
        self.year: int = attrs.get("year", 0)
        self.color: str = attrs.get("color", "null")
        self.category: str = attrs.get("category", "null")
        self.engine_type: str = attrs.get("engine_type", "null")
        self.seats: int = attrs.get("seats", 0)
        self.transmission: str = attrs.get("transmission", "null")
        self.top_speed: int = attrs.get("top_speed", 0)

    def __str__(self):
        return (
            f"{self.name} ({self.year}) - {self.make} {self.model}, {self.color}, "
            f"{self.category}, {self.engine_type}, {self.transmission}, "
            f"{self.seats} seats, Top Speed: {self.top_speed} km/h"
        )


class ScrapCars:
    def __init__(self, form_url: str, form_data: Dict[str, str]):
        self.form_url = form_url
        self.form_data = form_data

    def get_car_page(self) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Referer": "https://www.google.com/",
        }
        session = Session()
        session.headers.update(headers)
        return session.post(url=self.form_url, data=self.form_data)

    def scrap(self) -> Car:
        try:
            html_response = self.get_car_page()

        except Exception as e:
            raise Exception("Scrap Car Page Error: {e}")
