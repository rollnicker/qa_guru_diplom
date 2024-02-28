import allure

from diplom.web.application import app
from selene.core.query import text


@allure.title('2. Проверка добавление товара в просмотренные')
def test_visited_products(real_browser):
    app.open_page()
    with allure.step("Oткрыть каталог и выбрать Зима - Метеостанции"):
        kek = app.main_page.get_first_slider_item_name()
        app.main_page.open_first_slider_item()
        app.next_page().item_page.click_visited_prods_button()
        app.visited_page.should_first_item_name(kek)

