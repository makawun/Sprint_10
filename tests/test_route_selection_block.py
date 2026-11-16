import allure

from data.addresses import Addresses
from data.route_texts import RouteTexts


@allure.feature("Отрисовка блока с выбором маршрута")
class TestRouteSelectionBlock:

    @allure.title("При двух разных адресах отображается блок выбора маршрута")
    def test_block_visible_with_two_addresses(self, main_page, added_address_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Проверить, что отображается блок выбора маршрута"):
            assert added_address_page.is_route_block_visible()

    @allure.title("При одинаковых адресах показывается 'Авто Бесплатно В пути 0 мин.'")
    def test_same_address_message(self, main_page, added_address_page):
        with allure.step("Ввести одинаковые адреса в поля 'Откуда' и 'Куда'"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)
            main_page.enter_to_address(Addresses.FROM_ADDRESS)

        with allure.step("Проверить, что отображается блок выбора маршрута"):
            assert added_address_page.is_route_block_visible()

        with allure.step("Проверить, что в результате указано 'Авто Бесплатно'"):
            assert RouteTexts.SAME_ADDRESS_RESULT_TEXT in (
                added_address_page.get_result_text()
            )

        with allure.step("Проверить, что в результате указано 'В пути 0 мин.'"):
            assert RouteTexts.SAME_ADDRESS_DURATION in (
                added_address_page.get_duration()
            )

    @allure.title("Переключение между 'Оптимальный' и 'Быстрый' меняет активный таб")
    def test_switch_tabs_changes_active(self, main_page, added_address_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на вид маршрута 'Быстрый'"):
            added_address_page.click_fast_mode()

        with allure.step("Проверить, что активный таб — 'Быстрый'"):
            assert RouteTexts.FAST_MODE in added_address_page.get_active_tab_text()

        with allure.step("Переключиться на вид маршрута 'Оптимальный'"):
            added_address_page.click_optimum_mode()

        with allure.step("Проверить, что активный таб — 'Оптимальный'"):
            assert RouteTexts.OPTIMUM_MODE in added_address_page.get_active_tab_text()

    @allure.title("Переключение между табами пересчитывает стоимость и время маршрута")
    def test_switch_tabs_recalculates_cost_and_time(self, main_page, added_address_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Оптимальный' и запомнить результат"):
            added_address_page.click_optimum_mode()
            optimum_result = added_address_page.get_result_text()

        with allure.step("Переключиться на 'Быстрый' и запомнить результат"):
            added_address_page.click_fast_mode()
            fast_result = added_address_page.get_result_text()

        with allure.step("Проверить, что стоимость и время пересчитались"):
            assert optimum_result != fast_result, (
                "Текст результата (стоимость/время) не изменился при переключении таба"
            )

    @allure.title("В режиме 'Свой' активны все типы передвижения")
    def test_self_mode_shows_all_transport_types(self, main_page, added_address_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на вид маршрута 'Свой'"):
            added_address_page.click_self_mode()

        with allure.step("Проверить, что активны все типы передвижения"):
            assert added_address_page.is_car_type_visible()
            assert added_address_page.is_walk_type_visible()
            assert added_address_page.is_taxi_type_visible()
            assert added_address_page.is_bike_type_visible()
            assert added_address_page.is_scooter_type_visible()
            assert added_address_page.is_drive_type_visible()

    @allure.title("В режиме 'Быстрый' активна кнопка 'Вызвать такси'")
    def test_fast_mode_shows_call_taxi_button(self, main_page, added_address_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на вид маршрута 'Быстрый'"):
            added_address_page.click_fast_mode()

        with allure.step("Проверить, что отображается кнопка 'Вызвать такси'"):
            assert added_address_page.is_call_taxi_button_visible()

    @allure.title("В режиме 'Свой' + 'Драйв' активна кнопка 'Забронировать'")
    def test_self_drive_shows_book_button(self, main_page, added_address_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на вид маршрута 'Свой'"):
            added_address_page.click_self_mode()

        with allure.step("Выбрать тип передвижения 'Драйв'"):
            added_address_page.click_drive_type()

        with allure.step("Проверить, что отображается кнопка 'Забронировать'"):
            assert added_address_page.is_book_button_visible()

            