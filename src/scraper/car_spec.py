from requests import Session, Response
from typing import Dict
from selectolax import parser
from dotenv import load_dotenv
from pathlib import Path
from os import getenv

load_dotenv(dotenv_path=Path("../.env"))


class Car:
    def __init__(self, **attrs):
        self.name: str = attrs.get("name", "null")
        self.make: str = attrs.get("make", "null")
        self.model: str = attrs.get("model", "null")
        self.year: str = attrs.get("year", 0)
        self.color: str = attrs.get("color", "null")
        self.category: str = attrs.get("category", "null")
        self.engine_type: str = attrs.get("engine_type", "null")
        self.seats: int = attrs.get("seats", 0)
        self.transmission: str = attrs.get("transmission", "null")
        self.top_speed: str = attrs.get("top_speed", 0)

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
        self.car_obj = {}

    def get_car_page(self) -> None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Referer": "https://www.google.com/",
        }
        session = Session()
        session.headers.update(headers)
        response: Response = session.post(url=self.form_url, data=self.form_data)
        self.response = response.text

    def scrap(self) -> Car:
        try:
            self.get_car_page()
            car: Car = self.car_specification()
            return car
        except Exception as e:
            raise Exception(f"Scrap Car Page Error: {e}")

    def get_specification_table(self) -> None:
        tree = parser.HTMLParser(self.response)
        table = tree.tags(name="table")[0]
        trs = table.css("tr")
        first_tr = trs[0]
        third_d = first_tr.css("td:nth-child(3)")[0]
        tables = third_d.css("td > table")
        self.specification_table = tables[3]

    def get_name(self):
        paragraphs = self.specification_table.css("tr > td > center > p")
        car_name = paragraphs[0].css("font > b")[0].text(strip=True)
        self.car_obj["name"] = car_name

    def get_image(self):
        first_table = self.specification_table.css("tbody")[1]
        car_img = first_table.css("img")[1].attributes["data-src"]
        self.car_obj["image_url"] = getenv("SITE_SCRAPER") + car_img

    def get_car_information(self):
        first_table = self.specification_table.css("tr > td > font")[0]
        font_first = first_table.css_first("font")
        list_tables = font_first.css("font > font > table")
        table_spec = list_tables[2]
        tr = table_spec.css_first("tr")
        td = tr.css("td")[1]
        tables_inside = td.css("table")[1]
        first_tr = tables_inside.css_first("tr")
        left_spec = first_tr.css("tr > td")[0]
        right_spec = first_tr.css("tr > td")[1]
        trs_left = left_spec.css("table > tbody > tr:has(th)")
        trs_right = right_spec.css("table > tbody > tr:has(th)")
        trs_left = trs_left[3:]
        trs_right = trs_right[3:]
        self.get_car_spec_information(trs_left, self.car_obj)
        self.get_car_spec_information(trs_right, self.car_obj)

    def car_specification(
        self,
    ) -> Car:
        try:
            self.get_specification_table()
            self.get_name()
            self.get_image()
            self.get_car_information()
            data: Dict = {
                "name": self.car_obj["name"],
                "make": self.car_obj["make"],
                "model": self.car_obj["model"],
                "category": self.car_obj["class"],
                "engine_type": self.car_obj["engine type"],
                "transmission": self.car_obj["transmission type"],
                "top_speed": self.car_obj["top speed"],
            }
            car: Car = Car(**data)
            return car
        except Exception as e:
            raise ValueError(f"Error occur while getting Car specification: {e}")

    def get_car_spec_information(self, trs_to_process, car_information):
        for tr in trs_to_process:
            try:
                label = (
                    tr.css_first("th > p > font").text(strip=True).rstrip(":").lower()
                )
                value = tr.css_first("td > p > font").text(strip=True).rstrip(":")
                car_information[label] = value
            except Exception as e:
                pass
