from selene import browser, have


class HeaderMain:
    def __init__(self):
        self.header_logo = browser.element('.header-logo')
        self.visited_prods_button = browser.element('.header-top__link--brand')
        self.visited_prods_count = browser.all('.header-top__link--brand span')[1]
        self.login_button = browser.element('.header-top__link .fa-lock')

        self.cart_button = browser.element('.header-block .fa-shopping-cart')
        self.cart_count = browser.element('#in-cart-count-icon')

        self.catalog_button = browser.element('//*[text()="Каталог"]/parent::*')
        self.main_search = browser.element('#search-main')

        # проверить работоспособность
        self.address = browser.element('.header-block__main [href="contacts_article.html"]')
        self.company_search = browser.element('[tabindex="2"]')
        self.catalog_search = browser.element('[tabindex="3"]')

    def header_logo_click(self):
        self.header_logo.click()

    def open_visited_prods(self):
        self.visited_prods_button.click()

    def should_have_visited_prods_count(self, count):
        self.visited_prods_button.should(have.value(count))

    def open_catalog_menu(self):
        self.catalog_button.perform()


class HeaderMainScrolled:
    def __init__(self):
        self.box_header_logo = browser.element('.header-logo__image')
        self.box_address = browser.element('.header-block__icon .fa-map-marker')
        self.box_cart = browser.element('.header-block--cart')
        self.box_cart_count = browser.element('#in-cart-count')
        self.box_cart_sum = browser.element('#in-cart-sum')
        self.box_navbar_button = browser.element('.navbar__button')
        self.box_search = browser.element('#search-main')