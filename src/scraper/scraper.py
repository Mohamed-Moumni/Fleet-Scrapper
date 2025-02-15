from playwright.sync_api import sync_playwright, Frame, Page
from helpers import dump_frame_tree, filter_models
from dotenv import load_dotenv
from pathlib import Path
from bs4 import BeautifulSoup
from os import getenv
from typing import List, Dict
from tqdm import tqdm
from itertools import islice
from time import sleep
from car_spec import ScrapCars, Car

load_dotenv(dotenv_path=Path("../.env"))


class Scraper:
    def __init__(self, scrap_date: int, data_scrapped: List[str]) -> None:
        self.scrap_date = scrap_date
        self.data_scrapped = data_scrapped

    def browser_configuration(self) -> None:
        """
        Configures and launches the browser using Playwright.

        - Initializes a Firefox browser instance.
        - Opens a new page.
        - Navigates to the website specified in the environment variable `SITE_SCRAPER`.
        """
        self.browser = self.playwright.firefox.launch()
        self.page = self.browser.new_page()
        print("\033[32mGo To The Website\033[0m")
        self.page.goto(getenv("SITE_SCRAPER"), wait_until="load", timeout=120000)

    def get_main_frame(self) -> None:
        self.main_frame = dump_frame_tree(self.page.main_frame, "frame_aint_d")

    def get_model_cars_frame(self) -> None:
        self.car_frame = dump_frame_tree(self.page.main_frame, "ramka_modul_b")

    def scrap_cars_make(self) -> None:
        """
        Extracts all available makes, excluding the first default option.
        """
        print("\033[32mStart Scraping Cars Makes\n\033[0m")
        while self.main_frame.locator("#a > option:not([value='1'])").count() == 0:
            self.page.wait_for_timeout(500)

        makes = self.main_frame.locator("#a option:not([value='1'])").evaluate_all(
            """elements => elements.map(element => ({value:element.value}))"""
        )
        makes.pop(0)
        return makes

    def scrap_car_models(self, makes: List[Dict[str, str]]) -> None:
        """
        Scrapes available car models for each make.

        - Iterates through each make and selects it in the dropdown (`#a`).
        - Waits for models to load in the corresponding dropdown (`#b`).
        - Extracts and filters models before passing them to `scrap_car_sub_models`.

        Args:
            makes (List[Dict[str, str]]): A list of car makes with their values.
        """
        for make, _ in zip(makes, tqdm(range(len(makes)), desc="Makes Treated")):
            self.main_frame.select_option("#a", make["value"])
            while self.main_frame.locator("#b > option:not([value='1'])").count() == 0:
                self.page.wait_for_timeout(500)

            models: List[Dict[str, str]] = self.main_frame.locator(
                "#b > option:not([value='1'])"
            ).evaluate_all(
                """elements => elements.map(element => ({text:element.textContent.trim(), value: element.value}))"""
            )
            models.pop(0)
            filtered_models_by_year: List[str] = filter_models(models)
            self.scrap_car_sub_models(filtered_models_by_year)
            sleep(0.05)

    def scrap_car_sub_models(self, models: List[Dict[str, str]]) -> None:
        """
        Scrapes available sub-models for each car model.

        - Iterates through each model and selects it in the dropdown (`#b`).
        - Waits for sub-models to load in the corresponding dropdown (`#c`).
        - Extracts available sub-models.

        Args:
            models (List[str]): A list of car models.
        """

        self.get_model_cars_frame()
        for model in models:
            self.main_frame.select_option("#b", model)
            while self.main_frame.locator("#c > option:not([value='1'])").count() == 0:
                self.page.wait_for_timeout(500)

            sub_models = self.main_frame.locator(
                "#c > option:not([value='1'])"
            ).evaluate_all(
                """
                    elements => elements.map(element => ({
                    value: element.value
                    }))"""
            )
            sub_models.pop(0)
            for sub_model in sub_models:
                self.scrap_car(sub_model)

    def scrap_car(self, sub_model: Dict[str, str]) -> None:
        self.main_frame.select_option("#c", sub_model["value"])
        form = self.main_frame.locator("//form[@name='search_params1']")
        form.locator('input[type="submit"]').click()
        sleep(2)
        html_frame = self.car_frame.inner_html("html")
        soup = BeautifulSoup(str(html_frame), "html.parser")
        trs = soup.find_all("tr")
        for tr in trs:
            tds = tr.find_all("td")
            spec, year = islice(tds, 0, 4, 3)
            year = int(year.find("font").text)
            if year >= int(getenv("STARTING_SCRAP_YEAR")):
                form = spec.find("form")
                action_url = form["action"]
                form_data = {
                    input_tag["name"]: input_tag["value"]
                    for input_tag in form.find_all("input", {"type": "hidden"})
                }
                base_url = getenv("SITE_SCRAPER")
                full_url = base_url + action_url
                car_scraper = ScrapCars(full_url, form_data)
                car_scrapped: Car = car_scraper.scrap()
                print(car_scrapped)

    def start_scrap(self) -> None:
        """
        Initiates the car scraping process.

        - Launches the Playwright browser.
        - Retrieves the main frame.
        - Scrapes car makes, models, and sub-models.
        """
        with sync_playwright() as playwright:
            self.playwright = playwright
            self.browser_configuration()
            self.get_main_frame()
            makes: Dict[str, str] = self.scrap_cars_make()
            self.scrap_car_models(makes=makes)


if __name__ == "__main__":
    scrapper = Scraper(2024, ["name"])
    scrapper.start_scrap()
