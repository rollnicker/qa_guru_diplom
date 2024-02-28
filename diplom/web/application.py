import time

from selene import browser

from diplom.web.components.header_main import HeaderMain
from diplom.web.components.catalog import Catalog
from diplom.web.pages.catalog_page import CatalogPage
from diplom.web.pages.item_page import ItemPage
from diplom.web.pages.main_page import MainPage
from selene.core.query import text

from diplom.web.pages.viewed_items_page import VisitedPage


class Application:

    def __init__(self):
        self.header_main = HeaderMain()
        self.catalog_main = Catalog()
        self.main_page = MainPage()
        self.catalog_page = CatalogPage()
        self.item_page = ItemPage()
        self.visited_page = VisitedPage()

    def open_page(self):
        browser.open('')
        return self

    def next_page(self):
        browser.close()
        browser.switch_to_tab(0)
        time.sleep(5)
        return self

    def new_page(self):
        browser.switch_to_tab(1)
        time.sleep(5)
        return self

    # def scroll_down(self):
    #     browser.execute_script("window.scrollTo(0,600)")
    #     return self
    #
    # def switch_tab(self):
    #     browser.switch_to_next_tab()
    #     return self
    # def close_banner(self):
    #     if browser.element('.city-ask__wrapper').should(be.visible):
    #         browser.element('.city-ask__wrapper').element('.close-button').click()
    #     return self


app = Application()
