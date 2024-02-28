from selene import browser, have
from selene.core.query import text


class MainPage:
    def __init__(self):
        self.catalog_list_card = browser.all('.catalog-list__card')
        self.slider_item_card = browser.all('.product-list .slider__item')[0]
        self.slider_item_title = browser.all('.product-list .product-card__title')[0]

    def choose_catalog_category(self, catalog):
        self.catalog_list_card.element_by(have.text(catalog)).click()

    def get_first_slider_item_name(self):
        return self.slider_item_title.get(text)

    def open_first_slider_item(self):
        self.slider_item_card.click()

