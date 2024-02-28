from selene import browser, have
from selene.core.query import text


class CatalogPage:
    def __init__(self):
        self.list_title = browser.element('.list_head')
        self.list_first_item_name = browser.all('.item_name')[0]

    def should_have_title_name(self, name):
        self.list_title.should(have.text(name))

    def get_list_first_item_name(self):
        return self.list_first_item_name.get(text)

    def should_first_item_name(self, name):
        self.list_first_item_name.should(have.text(name))

    def open_first_item_page(self):
        self.list_first_item_name.click()
