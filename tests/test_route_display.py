import allure

from data.addresses import Addresses


@allure.feature("Отрисовка маршрута")
class TestRouteDisplay:

    @allure.title("При вводе двух разных адресов на карте видны обе точки")
    def test_map_shows_two_points(self, main_page, added_address_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Проверить, что на карте видны обе точки маршрута"):
            assert added_address_page.is_map_point_visible(
                Addresses.FROM_ADDRESS
            )
            assert added_address_page.is_map_point_visible(
                Addresses.TO_ADDRESS
            )

            