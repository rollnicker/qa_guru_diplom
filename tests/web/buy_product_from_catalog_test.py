import allure

from diplom.web.application import app


@allure.title('1. Прохождение по всему катологу и проверка покупки товара')
def test_buy_product_from_catalog(real_browser):
    app.open_page()
    with allure.step("Oткрыть каталог и выбрать Зима - Метеостанции"):
        app.header_main.catalog_button.click()
        app.catalog_main.select_catalog_category(category='Зима', subcategory='Метеостанции')
    with allure.step("Открыть страницу первого товара на странице каталога по категории"):
        app.next_page().catalog_page.should_have_title_name('Метеостанции')
        item_name = app.catalog_page.get_list_first_item_name()
        app.catalog_page.open_first_item_page()
    with allure.step("Нажать кнопку купить на странице товара"):
        app.next_page().item_page.should_have_name(f"{item_name}")
        app.item_page.press_buy_button()
    with allure.step("Проверяем что во всплывшем окне название продукта"):
        app.item_page.should_have_popup_text(f'{item_name}')

