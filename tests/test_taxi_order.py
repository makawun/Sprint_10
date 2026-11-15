import allure

from data.addresses import Addresses
from data.taxi_texts import TaxiTexts
from helper import extract_price_number


@allure.feature("Заказ тарифа Такси")
class TestTaxiOrder:

    @allure.title("После заказа открывается окно ожидания со всеми элементами")
    def test_waiting_window_elements(self, order_placed, waiting_taxi_page):
        assert waiting_taxi_page.is_header_visible()
        assert waiting_taxi_page.is_timer_visible()
        assert waiting_taxi_page.is_cancel_visible()
        assert waiting_taxi_page.is_details_visible()

    @allure.title("После окончания таймера открывается окно совершенного заказа")
    def test_complete_window_appears(self, confirmed_order, confirm_order_page):
        assert confirm_order_page.is_confirm_header_visible()
        assert confirm_order_page.is_car_number_visible()
        assert confirm_order_page.is_car_image_visible()
        assert confirm_order_page.is_rating_visible()
        assert confirm_order_page.is_driver_image_visible()
        assert confirm_order_page.is_driver_name_visible()
        assert confirm_order_page.is_cancel_visible()
        assert confirm_order_page.is_details_visible()

    @allure.title("В деталях указана стоимость, совпадающая с ценой выбранного тарифа")
    def test_details_price_matches_tariff_price(self, confirmed_order, tariff_price,
                                                confirm_order_page):
        confirm_order_page.click_details()

        assert confirm_order_page.is_details_block_visible()
        assert extract_price_number(tariff_price) in extract_price_number(
            confirm_order_page.get_price()
        )

    @allure.title("Кнопка 'Отмена' закрывает окно заказа")
    def test_cancel_closes_window(self, confirmed_order, confirm_order_page):
        confirm_order_page.click_cancel()

        assert confirm_order_page.is_window_closed()

    @allure.title("Полный флоу: от ввода адресов до закрытия окна заказа")
    def test_full_taxi_order_flow(self, main_page, added_address_page,
                                  taxi_page, waiting_taxi_page,
                                  confirm_order_page):
        main_page.enter_from_address(Addresses.FROM_ADDRESS)
        main_page.enter_to_address(Addresses.TO_ADDRESS)

        added_address_page.click_fast_mode()
        added_address_page.click_call_taxi()

        taxi_page.select_tariff(TaxiTexts.DEFAULT_ORDER_TARIFF)
        taxi_page.toggle_laptop_table()
        taxi_page.click_order()

        assert waiting_taxi_page.is_header_visible()
        confirm_order_page.wait_confirm_header()
        assert confirm_order_page.is_car_number_visible()

        confirm_order_page.click_cancel()
        assert confirm_order_page.is_window_closed()

