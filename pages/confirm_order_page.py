from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.confirm_order_page_locators import ConfirmOrderPageLocators
from pages.base_page import BasePage


class ConfirmOrderPage(BasePage):
    def wait_confirm_header(self, timeout=120, settle_pause=1.0):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(
                ConfirmOrderPageLocators.CONFIRM_HEADER
            )
        )
        self.pause(settle_pause)
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(
                ConfirmOrderPageLocators.CONFIRM_HEADER
            )
        )

    def click_details(self, timeout=30):
        self.js_click(ConfirmOrderPageLocators.DETAILS_BUTTON)
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(
                ConfirmOrderPageLocators.DETAILS_BLOCK
            )
        )

    def click_cancel(self):
        self.click(ConfirmOrderPageLocators.CANCEL_BUTTON)

    def is_details_block_visible(self, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(
                    ConfirmOrderPageLocators.DETAILS_BLOCK
                )
            )
            return True
        except TimeoutException:
            return False

    def is_confirm_header_visible(self, timeout=30):
        return self.is_present(
            ConfirmOrderPageLocators.CONFIRM_HEADER, timeout=timeout
        )

    def is_window_closed(self, timeout=10):
        return self.is_gone(
            ConfirmOrderPageLocators.HEADER, timeout=timeout
        )

    def is_car_number_visible(self, timeout=30):
        return self.is_present(
            ConfirmOrderPageLocators.AUTOMOBILE_NUMBER, timeout=timeout
        )

    def is_car_image_visible(self, timeout=30):
        return self.is_present(
            ConfirmOrderPageLocators.AUTOMOBILE_IMG, timeout=timeout
        )

    def is_rating_visible(self, timeout=30):
        return self.is_present(ConfirmOrderPageLocators.RATE, timeout=timeout)

    def is_driver_image_visible(self, timeout=30):
        return self.is_present(ConfirmOrderPageLocators.DRIVER_IMG, timeout=timeout)

    def is_driver_name_visible(self, timeout=30):
        return self.is_present(ConfirmOrderPageLocators.DRIVER_NAME, timeout=timeout)

    def is_cancel_visible(self, timeout=30):
        return self.is_present(ConfirmOrderPageLocators.CANCEL_BUTTON, timeout=timeout)

    def is_details_visible(self, timeout=30):
        return self.is_present(ConfirmOrderPageLocators.DETAILS_BUTTON, timeout=timeout)

    def get_price(self):
        return self.get_text(ConfirmOrderPageLocators.PRICE)

    