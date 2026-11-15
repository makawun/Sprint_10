import allure

from data.route_texts import RouteTexts


@allure.feature("Отрисовка блока с выбором маршрута")
class TestRouteSelectionBlock:

    @allure.title("При двух разных адресах отображается блок выбора маршрута")
    def test_block_visible_with_two_addresses(self, addresses_entered, added_address_page):
        assert added_address_page.is_route_block_visible()

    @allure.title("При одинаковых адресах показывается 'Авто Бесплатно В пути 0 мин.'")
    def test_same_address_message(self, same_address_entered, added_address_page):
        assert added_address_page.is_route_block_visible()
        assert RouteTexts.SAME_ADDRESS_RESULT_TEXT in added_address_page.get_result_text()
        assert RouteTexts.SAME_ADDRESS_DURATION in added_address_page.get_duration()

    @allure.title("Переключение между 'Оптимальный' и 'Быстрый' меняет активный таб")
    def test_switch_tabs_changes_active(self, addresses_entered, added_address_page):
        added_address_page.click_fast_mode()
        assert RouteTexts.FAST_MODE in added_address_page.get_active_tab_text()

        added_address_page.click_optimum_mode()
        assert RouteTexts.OPTIMUM_MODE in added_address_page.get_active_tab_text()

    @allure.title("Переключение между табами пересчитывает стоимость и время маршрута")
    def test_switch_tabs_recalculates_cost_and_time(self, addresses_entered, added_address_page):
        added_address_page.click_optimum_mode()
        optimum_result = added_address_page.get_result_text()

        added_address_page.click_fast_mode()
        fast_result = added_address_page.get_result_text()

        assert optimum_result != fast_result, (
            "Текст результата (стоимость/время) не изменился при переключении таба"
        )

    @allure.title("В режиме 'Свой' активны все типы передвижения")
    def test_self_mode_shows_all_transport_types(self, addresses_entered, added_address_page):
        added_address_page.click_self_mode()

        assert added_address_page.is_car_type_visible()
        assert added_address_page.is_walk_type_visible()
        assert added_address_page.is_taxi_type_visible()
        assert added_address_page.is_bike_type_visible()
        assert added_address_page.is_scooter_type_visible()
        assert added_address_page.is_drive_type_visible()

    @allure.title("В режиме 'Быстрый' активна кнопка 'Вызвать такси'")
    def test_fast_mode_shows_call_taxi_button(self, addresses_entered, added_address_page):
        added_address_page.click_fast_mode()
        assert added_address_page.is_call_taxi_button_visible()

    @allure.title("В режиме 'Свой' + 'Драйв' активна кнопка 'Забронировать'")
    def test_self_drive_shows_book_button(self, addresses_entered, added_address_page):
        added_address_page.click_self_mode()
        added_address_page.click_drive_type()
        assert added_address_page.is_book_button_visible()

        