from typing import List
from playwright.sync_api import sync_playwright, Frame, Page
from helpers import dump_frame_tree



class Scraper:
    def __init__(self, scrap_date:int, data_scrapped:List[str]) -> None:
        self.scrap_date = scrap_date
        self.data_scrapped = data_scrapped
    
    def browser_configuration(self) -> None:
        self.browser = self.playwright.firefox.launch()
        self.page = self.browser.new_page()
        self.page.goto("https://www.automobile-catalog.com/", wait_until='load')
        
    def get_main_frame(self) -> None:
        self.main_frame = dump_frame_tree(self.page.main_frame)
        
    def scrap_cars_make(self) -> None:
        while self.main_frame.locator("#a > option:not([value='1'])").count() == 0:
            self.page.wait_for_timeout(500)
            
        makes = self.main_frame.locator("#a option:not([value='1'])").evaluate_all("""elements => elements.map(element => ({value:element.value}))""")
        makes.pop(0)
        return makes

    def scrap_car_models(self) -> None:
        pass
    
    def scrap_car_sub_models(self) -> None:
        pass
    
    def start_scrap(self) -> None:
        with sync_playwright() as playwright:
            self.playwright = playwright
            self.browser_configuration()
            self.get_main_frame()
            print(self.scrap_cars_make())


if __name__ == "__main__":
    scrapper = Scraper(2024, ['name'])
    scrapper.start_scrap()
    
    