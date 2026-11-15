import allure

from data.addresses import Addresses


@allure.feature("Отрисовка маршрута")
class TestRouteDisplay:

    @allure.title("При вводе двух разных адресов на карте видны обе точки")
    def test_map_shows_two_points(self, addresses_entered, added_address_page):
        assert added_address_page.is_map_point_visible(Addresses.FROM_ADDRESS)
        assert added_address_page.is_map_point_visible(Addresses.TO_ADDRESS)