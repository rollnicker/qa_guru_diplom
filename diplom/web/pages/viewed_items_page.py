from selene import browser, have
from selene.core.query import text


class VisitedPage:
    def __init__(self):
        self.list_first_item_name = browser.all('[itemprop="name"]')

    def should_first_item_name(self, text):
        self.list_first_item_name.should(have.text(text))
