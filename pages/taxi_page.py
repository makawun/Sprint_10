from data.taxi_texts import TaxiTexts
from locators.taxi_page_locators import TaxiPageLocators
from pages.base_page import BasePage


class TaxiPage(BasePage):
    def _format(self, locator, tariff_name):
        return (locator[0], locator[1].format(tariff_name=tariff_name))

    def get_tariffs_count(self):
        return len(self.find_all(TaxiPageLocators.TCARD))

    def get_active_tariffs_count(self):
        return len(self.find_all(TaxiPageLocators.TCARD_WORK))

    def get_tariff_price(self, tariff_name, timeout=10):
        locator = self._format(TaxiPageLocators.TARIFF_PRICE, tariff_name)
        self.wait_text_not_empty(locator, timeout)
        return self.get_text(locator)

    def select_tariff(self, tariff_name, timeout=10):
        self.js_click(self._format(TaxiPageLocators.TARIFF_CARD, tariff_name))
        self.wait_presence(
            self._format(TaxiPageLocators.ACTIVE_TARIFF_CARD, tariff_name),
            timeout,
        )
        self.pause(0.7)

    def hover_tariff_info(self, tariff_name, attempts=3, timeout=15):
        locator = self._format(TaxiPageLocators.INFORMATION_BUTTON, tariff_name)
        self.wait_visible(locator, timeout=10)
        reset_locator = self._format(
            TaxiPageLocators.TCARD, TaxiTexts.DEFAULT_ORDER_TARIFF
        )
        for _ in range(attempts):
            self.hover(locator)
            if self.is_tooltip_visible(tariff_name, timeout=timeout):
                return
            self.hover(reset_locator)
        self.hover(locator)

    def is_tooltip_visible(self, tariff_name, timeout=15):
        locator = self._format(TaxiPageLocators.TOOLTIP, tariff_name)
        return self.is_visible(locator, timeout)

    def get_tooltip_text(self, tariff_name):
        return self.get_text(self._format(TaxiPageLocators.TOOLTIP, tariff_name))

    def is_info_button_present(self, tariff_name):
        return self.is_present(
            self._format(TaxiPageLocators.INFORMATION_BUTTON, tariff_name)
        )

    def is_phone_visible(self):
        return self.is_present(TaxiPageLocators.PHONE_NUMBER)

    def is_payment_visible(self):
        return self.is_present(TaxiPageLocators.PAYMENT)

    def is_comment_visible(self):
        return self.is_present(TaxiPageLocators.COMMENT)

    def is_requirements_visible(self):
        return self.is_present(TaxiPageLocators.REQUIREMENTS)

    def toggle_laptop_table(self):
        self.js_click(TaxiPageLocators.LAPTOP_TABLE)

    def click_order(self):
        self.click(TaxiPageLocators.ORDER_BUTTON)

        