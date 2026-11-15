from data.route_texts import RouteTexts
from locators.added_address_page_locators import AddedAddressPageLocators
from pages.base_page import BasePage


class AddedAddressPage(BasePage):
    def is_map_point_visible(self, address):
        locator = (
            AddedAddressPageLocators.YMAP[0],
            AddedAddressPageLocators.YMAP[1].format(address=address),
        )
        return self.is_present(locator, timeout=15)

    def is_route_block_visible(self):
        return self.is_present(AddedAddressPageLocators.ROUTE_BLOCK)

    def get_result_text(self):
        return self.get_text(AddedAddressPageLocators.RESULT_TEXT)

    def get_duration(self):
        return self.get_text(AddedAddressPageLocators.DURATION)

    def click_optimum_mode(self):
        self.click(AddedAddressPageLocators.OPTIMUM_ROUTE_MODE)

    def click_fast_mode(self):
        self.click(AddedAddressPageLocators.FAST_ROUTE_MODE)

    def click_self_mode(self):
        self.click(AddedAddressPageLocators.SELF_ROUTE_MODE)

    def get_active_tab_text(self):
        return self.get_text(AddedAddressPageLocators.ACTIVE_TAB)

    def is_car_type_visible(self):
        return self.is_present(AddedAddressPageLocators.CAR_TYPE)

    def is_walk_type_visible(self):
        return self.is_present(AddedAddressPageLocators.WALK_TYPE)

    def is_taxi_type_visible(self):
        return self.is_present(AddedAddressPageLocators.TAXI_TYPE)

    def is_bike_type_visible(self):
        return self.is_present(AddedAddressPageLocators.BIKE_TYPE)

    def is_scooter_type_visible(self):
        return self.is_present(AddedAddressPageLocators.SCOOTER_TYPE)

    def is_drive_type_visible(self):
        return self.is_present(AddedAddressPageLocators.DRIVE_TYPE)

    def click_drive_type(self):
        self.click(AddedAddressPageLocators.DRIVE_TYPE)

    def _action_button(self, button_text):
        return (
            AddedAddressPageLocators.ACTION_BUTTON[0],
            AddedAddressPageLocators.ACTION_BUTTON[1].format(
                button_text=button_text
            ),
        )

    def is_call_taxi_button_visible(self):
        return self.is_present(
            self._action_button(RouteTexts.CALL_TAXI_BUTTON_TEXT)
        )

    def is_book_button_visible(self):
        return self.is_present(
            self._action_button(RouteTexts.BOOK_BUTTON_TEXT)
        )

    def click_call_taxi(self):
        self.click(self._action_button(RouteTexts.CALL_TAXI_BUTTON_TEXT))

        