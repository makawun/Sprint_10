import allure
import pytest

from data.addresses import Addresses
from data.taxi_cases import (
    TAXI_TARIFF_CASES,
    TAXI_TARIFF_MATCH_CASES,
    TAXI_TARIFF_NAMES,
)
from data.taxi_texts import TaxiTexts


@allure.feature("Подготовка к заказу такси")
class TestTaxiPreparation:

    @allure.title("Форма заказа открывается со всеми 6 тарифами из ТЗ")
    def test_six_tariffs_displayed(self, main_page, added_address_page, taxi_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Быстрый' и открыть форму заказа такси"):
            added_address_page.click_fast_mode()
            added_address_page.click_call_taxi()

        with allure.step("Проверить, что отображается 6 тарифов"):
            assert taxi_page.get_tariffs_count() == TaxiTexts.TAXI_TARIFFS_COUNT

    @allure.title("Один из тарифов активен по умолчанию")
    def test_one_active_tariff(self, main_page, added_address_page, taxi_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Быстрый' и открыть форму заказа такси"):
            added_address_page.click_fast_mode()
            added_address_page.click_call_taxi()

        with allure.step("Проверить, что активен ровно один тариф"):
            assert (
                taxi_page.get_active_tariffs_count()
                == TaxiTexts.ACTIVE_TARIFFS_COUNT
            )

    @allure.title("Иконка i присутствует в DOM у каждого тарифа")
    @pytest.mark.parametrize("tariff_name", TAXI_TARIFF_NAMES)
    def test_info_button_present_on_each_tariff(self, main_page, added_address_page,
                                                taxi_page, tariff_name):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Быстрый' и открыть форму заказа такси"):
            added_address_page.click_fast_mode()
            added_address_page.click_call_taxi()

        with allure.step(f"Проверить, что у тарифа '{tariff_name}' есть иконка i"):
            assert taxi_page.is_info_button_present(tariff_name)

    @allure.title("При наведении на иконку i активного тарифа '{tariff_name}' появляется тултип")
    @pytest.mark.parametrize("tariff_name, _expected", TAXI_TARIFF_CASES)
    def test_tariff_tooltip_appears(self, main_page, added_address_page, taxi_page,
                                    tariff_name, _expected):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Быстрый' и открыть форму заказа такси"):
            added_address_page.click_fast_mode()
            added_address_page.click_call_taxi()

        with allure.step(f"Активировать тариф '{tariff_name}'"):
            taxi_page.select_tariff(tariff_name)

        with allure.step(f"Навести курсор на иконку i тарифа '{tariff_name}'"):
            taxi_page.hover_tariff_info(tariff_name)

        with allure.step("Проверить, что тултип отображается"):
            assert taxi_page.is_tooltip_visible(tariff_name)

    @allure.title("Описание активного тарифа '{tariff_name}' в тултипе соответствует ТЗ")
    @pytest.mark.parametrize("tariff_name, expected_description", TAXI_TARIFF_MATCH_CASES)
    def test_tariff_tooltip_matches_tz(self, main_page, added_address_page, taxi_page,
                                       tariff_name, expected_description):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Быстрый' и открыть форму заказа такси"):
            added_address_page.click_fast_mode()
            added_address_page.click_call_taxi()

        with allure.step(f"Активировать тариф '{tariff_name}'"):
            taxi_page.select_tariff(tariff_name)

        with allure.step(f"Навести курсор на иконку i тарифа '{tariff_name}'"):
            taxi_page.hover_tariff_info(tariff_name)

        with allure.step("Проверить, что тултип отображается"):
            assert taxi_page.is_tooltip_visible(tariff_name)

        with allure.step("Проверить, что описание в тултипе соответствует ТЗ"):
            assert expected_description in taxi_page.get_tooltip_text(tariff_name)

    @allure.title("Под тарифами отображаются поля формы заказа")
    def test_form_fields_visible(self, main_page, added_address_page, taxi_page):
        with allure.step("Ввести адрес отправления"):
            main_page.enter_from_address(Addresses.FROM_ADDRESS)

        with allure.step("Ввести адрес назначения"):
            main_page.enter_to_address(Addresses.TO_ADDRESS)

        with allure.step("Переключиться на 'Быстрый' и открыть форму заказа такси"):
            added_address_page.click_fast_mode()
            added_address_page.click_call_taxi()

        with allure.step("Проверить, что отображаются поля формы заказа"):
            assert taxi_page.is_phone_visible()
            assert taxi_page.is_payment_visible()
            assert taxi_page.is_comment_visible()
            assert taxi_page.is_requirements_visible()

            