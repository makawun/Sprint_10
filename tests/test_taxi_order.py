import allure

from data.addresses import Addresses
from data.taxi_texts import TaxiTexts
from helper import extract_price_number


@allure.feature("Заказ тарифа Такси")
class TestTaxiOrder:

    @allure.title("После заказа открывается окно ожидания со всеми элементами")
    def test_waiting_window_elements(self, main_page, added_address_page,
                                     taxi_page, waiting_taxi_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Быстрый' и открыть форму заказа такси"):
            added_address_page.click_fast_mode()
            added_address_page.click_call_taxi()

        with allure.step(f"Выбрать тариф '{TaxiTexts.DEFAULT_ORDER_TARIFF}'"):
            taxi_page.select_tariff(TaxiTexts.DEFAULT_ORDER_TARIFF)

        with allure.step("Включить чекбокс 'Столик для ноутбука'"):
            taxi_page.toggle_laptop_table()

        with allure.step("Нажать 'Ввести номер и заказать'"):
            taxi_page.click_order()

        with allure.step("Проверить элементы окна ожидания машины"):
            assert waiting_taxi_page.is_header_visible()
            assert waiting_taxi_page.is_timer_visible()
            assert waiting_taxi_page.is_cancel_visible()
            assert waiting_taxi_page.is_details_visible()

    @allure.title("После окончания таймера открывается окно совершенного заказа")
    def test_complete_window_appears(self, main_page, added_address_page, taxi_page,
                                     confirm_order_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Быстрый' и открыть форму заказа такси"):
            added_address_page.click_fast_mode()
            added_address_page.click_call_taxi()

        with allure.step(f"Выбрать тариф '{TaxiTexts.DEFAULT_ORDER_TARIFF}'"):
            taxi_page.select_tariff(TaxiTexts.DEFAULT_ORDER_TARIFF)

        with allure.step("Включить чекбокс 'Столик для ноутбука'"):
            taxi_page.toggle_laptop_table()

        with allure.step("Нажать 'Ввести номер и заказать'"):
            taxi_page.click_order()

        with allure.step("Дождаться открытия окна совершенного заказа"):
            confirm_order_page.wait_confirm_header()

        with allure.step("Проверить элементы окна совершенного заказа"):
            assert confirm_order_page.is_confirm_header_visible()
            assert confirm_order_page.is_car_number_visible()
            assert confirm_order_page.is_car_image_visible()
            assert confirm_order_page.is_rating_visible()
            assert confirm_order_page.is_driver_image_visible()
            assert confirm_order_page.is_driver_name_visible()
            assert confirm_order_page.is_cancel_visible()
            assert confirm_order_page.is_details_visible()

    @allure.title("В деталях указана стоимость, совпадающая с ценой выбранного тарифа")
    def test_details_price_matches_tariff_price(self, main_page, added_address_page,
                                                taxi_page, confirm_order_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Быстрый' и открыть форму заказа такси"):
            added_address_page.click_fast_mode()
            added_address_page.click_call_taxi()

        with allure.step(f"Запомнить цену тарифа '{TaxiTexts.DEFAULT_ORDER_TARIFF}'"):
            tariff_price = taxi_page.get_tariff_price(TaxiTexts.DEFAULT_ORDER_TARIFF)

        with allure.step(f"Выбрать тариф '{TaxiTexts.DEFAULT_ORDER_TARIFF}'"):
            taxi_page.select_tariff(TaxiTexts.DEFAULT_ORDER_TARIFF)

        with allure.step("Включить чекбокс 'Столик для ноутбука'"):
            taxi_page.toggle_laptop_table()

        with allure.step("Нажать 'Ввести номер и заказать'"):
            taxi_page.click_order()

        with allure.step("Дождаться открытия окна совершенного заказа"):
            confirm_order_page.wait_confirm_header()

        with allure.step("Открыть детали заказа"):
            confirm_order_page.click_details()

        with allure.step("Проверить, что в деталях указана цена выбранного тарифа"):
            assert confirm_order_page.is_details_block_visible()
            assert extract_price_number(tariff_price) in extract_price_number(
                confirm_order_page.get_price()
            )

    @allure.title("Кнопка 'Отмена' закрывает окно заказа")
    def test_cancel_closes_window(self, main_page, added_address_page, taxi_page,
                                  confirm_order_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Быстрый' и открыть форму заказа такси"):
            added_address_page.click_fast_mode()
            added_address_page.click_call_taxi()

        with allure.step(f"Выбрать тариф '{TaxiTexts.DEFAULT_ORDER_TARIFF}'"):
            taxi_page.select_tariff(TaxiTexts.DEFAULT_ORDER_TARIFF)

        with allure.step("Включить чекбокс 'Столик для ноутбука'"):
            taxi_page.toggle_laptop_table()

        with allure.step("Нажать 'Ввести номер и заказать'"):
            taxi_page.click_order()

        with allure.step("Дождаться открытия окна совершенного заказа"):
            confirm_order_page.wait_confirm_header()

        with allure.step("Нажать 'Отмена'"):
            confirm_order_page.click_cancel()

        with allure.step("Проверить, что окно закрылось"):
            assert confirm_order_page.is_window_closed()

    @allure.title("Полный флоу: от ввода адресов до закрытия окна заказа")
    def test_full_taxi_order_flow(self, main_page, added_address_page, taxi_page,
                                  waiting_taxi_page, confirm_order_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Быстрый' и открыть форму заказа такси"):
            added_address_page.click_fast_mode()
            added_address_page.click_call_taxi()

        with allure.step(f"Выбрать тариф '{TaxiTexts.DEFAULT_ORDER_TARIFF}'"):
            taxi_page.select_tariff(TaxiTexts.DEFAULT_ORDER_TARIFF)

        with allure.step("Включить чекбокс 'Столик для ноутбука'"):
            taxi_page.toggle_laptop_table()

        with allure.step("Нажать 'Ввести номер и заказать'"):
            taxi_page.click_order()

        with allure.step("Проверить, что открылось окно ожидания машины"):
            assert waiting_taxi_page.is_header_visible()

        with allure.step("Дождаться открытия окна совершенного заказа"):
            confirm_order_page.wait_confirm_header()

        with allure.step("Проверить, что в окне заказа отображается номер автомобиля"):
            assert confirm_order_page.is_car_number_visible()

        with allure.step("Нажать 'Отмена'"):
            confirm_order_page.click_cancel()

        with allure.step("Проверить, что окно закрылось"):
            assert confirm_order_page.is_window_closed()