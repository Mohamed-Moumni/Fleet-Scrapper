import click
import requests


@click.group()
def main_group():
    """Main command group"""
    pass


@click.command(name="search")
@click.option(
    "--make",
    prompt="Enter the make you are searching for",
    help="The make you are searching for",
)
@click.option(
    "--model",
    prompt="Enter the model you are searching for",
    help="The model you are searching for",
)
@click.option(
    "--sub-model",
    prompt="Enter the sub-model you are searching for",
    help="The Sub-model you are searching for",
)
def search_car_cmd(make: str, model: str, sub_model: str):
    """Search for a car"""
    click.echo(f"Searching for {make} {model} {sub_model}...")


@click.command(name="extract")
@click.option(
    "--extract",
    prompt="Enter the type of data that you extract with (json, csv)",
    help="Type of data to extract with (csv, json)",
)
def extract_data(extract: str):
    """Extract data in a specific format"""
    click.echo(f"Extracting data as {extract}...")


main_group.add_command(search_car_cmd)
main_group.add_command(extract_data)

if __name__ == "__main__":
    main_group()
