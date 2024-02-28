from selene import browser, have, command
from selene.core.query import text

from diplom.web.pages.main_page import MainPage


class ItemPage:
    def __init__(self):
        self.product_name = browser.element('.product_title')
        self.buy_item_button = browser.element('//*[text()="Купить"]/parent::*')
        self.buy_buttons = browser.all('.product_price_div')[0]
        self.common_price = browser.element('//*[text()="Купить"]/parent::*/parent::*/div[@class="price"]')
        self.popup = browser.element('.popup_self')
        self.visited_prods_button = browser.element('.visited_prods')
        self.pleer_logo = browser.element('.logo')

    def should_have_name(self, name):
        self.product_name.should(have.text(name))

    def press_buy_button(self):
        self.buy_buttons.perform(command.js.scroll_into_view)
        self.buy_item_button.click()
        '''Спросить почему команда perform не находит item_button'''

    def should_have_popup_text(self, name):
        self.popup.should(have.text(name))

    def click_logo(self):
        self.pleer_logo.click()
        return MainPage()

    def click_visited_prods_button(self):
        self.visited_prods_button.double_click()

    def should_have_visited_prods_count(self, count):
        self.visited_prods_button.should(have.text(count))

...


def get_product_item_name(self):
    return self.product_name.get(text)


'''Не факт что нужно '''


def get_popup_text(self):
    return self.popup.get(text)


'''Не факт что нужно'''


def get_product_price(self):
    return self.common_price.get(text)


'''Не работает, так как выводит две цены (со скидкой и без)'''
