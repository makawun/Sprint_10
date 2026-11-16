from locators.waiting_taxi_page_locators import WaitingTaxiPageLocators
from pages.base_page import BasePage


class WaitingTaxiPage(BasePage):
    def is_header_visible(self):
        return self.is_present(WaitingTaxiPageLocators.HEADER)

    def is_timer_visible(self):
        return self.is_present(WaitingTaxiPageLocators.TIMER)

    def is_cancel_visible(self):
        return self.is_present(WaitingTaxiPageLocators.CANCEL_BUTTON)

    def is_details_visible(self):
        return self.is_present(WaitingTaxiPageLocators.DETAILS_BUTTON)

    