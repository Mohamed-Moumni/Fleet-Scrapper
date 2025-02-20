import click
from tabulate import tabulate
import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXPORT_FOLDER = os.path.join(os.getcwd(), "data_export")
from scraper.services import Service


def show_data(data, headers, tablefmt="grid"):
    print(data)
    print(tabulate(data, headers, tablefmt))


def fetch_data(make: str, model: str, sub_model: str, category: str):
    service = Service()
    params = {}
    if make:
        params["make"] = make
    if model:
        params["model"] = model
    if sub_model:
        params["sub_mode"] = sub_model
    if category:
        params["category"] = category
    cars = service.get_car_spec(**params)
    return cars


@click.group()
def main_group():
    """Main command group"""
    pass


@click.command(name="search")
@click.option(
    "--make",
    prompt="Enter the make you are searching for",
    default="",
    show_default=False,
    help="The make you are searching for",
)
@click.option(
    "--model",
    prompt="Enter the model you are searching for",
    default="",
    show_default=False,
    help="The model you are searching for",
)
@click.option(
    "--sub-model",
    prompt="Enter the sub-model you are searching for",
    default="",
    show_default=False,
    help="The Sub-model you are searching for",
)
@click.option(
    "--category",
    prompt="Enter the category you are searching for",
    default="",
    show_default=False,
    help="The Category you are searching for",
)
def search_car_cmd(make: str, model: str, sub_model: str, category: str):
    """Search for a car"""
    cars = fetch_data(make, model, sub_model, category)
    cars = format_data_for_output(cars)
    headers = [
        "id",
        "name",
        "make",
        "sub_model",
        "model",
        "year",
        "color",
        "category",
        "engine_type",
        "seats",
        "transmission",
        "top_speed",
    ]
    show_data(cars, headers)


def format_data_for_output(data):
    return [
        [
            item["id"],
            item["name"],
            item["make"],
            item["sub_model"],
            item["model"],
            item["year"],
            item["color"],
            item["category"],
            item["engine_type"],
            item["seats"],
            item["transmission"],
            item["top_speed"],
        ]
        for item in data
    ]


@click.command(name="extract")
@click.option(
    "--extract",
    prompt="Enter the type of data that you extract with (json, csv)",
    help="Type of data to extract with (csv, json)",
)
@click.option(
    "--make",
    prompt="Enter the make you are searching for",
    default="",
    show_default=False,
    help="The make you are searching for",
)
@click.option(
    "--model",
    prompt="Enter the model you are searching for",
    default="",
    show_default=False,
    help="The model you are searching for",
)
@click.option(
    "--sub-model",
    prompt="Enter the sub-model you are searching for",
    default="",
    show_default=False,
    help="The Sub-model you are searching for",
)
@click.option(
    "--category",
    prompt="Enter the category you are searching for",
    default="",
    show_default=False,
    help="The Category you are searching for",
)
def extract_data(extract: str, make: str, model: str, sub_model: str, category: str):
    """Extract data in a specific format"""
    if extract not in ["json", "csv"]:
        print("Invalid Error you Must Enter one of the Following Values: (json, csv)")
    elif extract == "json":
        cars = fetch_data(make, model, sub_model, category)
        file_name = os.path.join(EXPORT_FOLDER, "car_data.json")
        with open(file_name, "w") as file:
            json.dump(cars, file, indent=4)
        print(f"Json File format is Successfully Exported '{file_name}'")
    else:
        pass


main_group.add_command(search_car_cmd)
main_group.add_command(extract_data)

if __name__ == "__main__":
    main_group()
