from selene import browser, have


class Catalog:
    def __init__(self):
        self.catalog_category = browser.all('.navbar__drop .catalog-list__title')
        self.catalog_menu_item = browser.all('.navbar__drop .catalog-menu__title')

    def select_catalog_category(self, category, subcategory):
        self.catalog_category.element_by(have.text(f'{category}')).click()
        self.catalog_menu_item.element_by(have.text(f'{subcategory}')).click()
