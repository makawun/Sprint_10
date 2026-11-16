from data.urls import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def open(self):
        super().open(Urls.SERVICE_URL)

    def enter_from_address(self, address):
        self.type_text_and_enter(MainPageLocators.FROM_INPUT, address)

    def enter_to_address(self, address):
        self.type_text_and_enter(MainPageLocators.TO_INPUT, address)