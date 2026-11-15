import allure
import pytest

from data.taxi_cases import (
    TAXI_TARIFF_CASES,
    TAXI_TARIFF_MATCH_CASES,
    TAXI_TARIFF_NAMES,
)
from data.taxi_texts import TaxiTexts


@allure.feature("Подготовка к заказу такси")
class TestTaxiPreparation:

    @allure.title("Форма заказа открывается со всеми 6 тарифами из ТЗ")
    def test_six_tariffs_displayed(self, taxi_form_opened, taxi_page):
        assert taxi_page.get_tariffs_count() == TaxiTexts.TAXI_TARIFFS_COUNT

    @allure.title("Один из тарифов активен по умолчанию")
    def test_one_active_tariff(self, taxi_form_opened, taxi_page):
        assert taxi_page.get_active_tariffs_count() == TaxiTexts.ACTIVE_TARIFFS_COUNT

    @allure.title("Иконка i присутствует в DOM у каждого тарифа")
    @pytest.mark.parametrize("tariff_name", TAXI_TARIFF_NAMES)
    def test_info_button_present_on_each_tariff(self, taxi_form_opened, taxi_page,
                                                tariff_name):
        assert taxi_page.is_info_button_present(tariff_name)

    @allure.title("При наведении на иконку i активного тарифа '{tariff_name}' появляется тултип")
    @pytest.mark.parametrize("tariff_name, _expected", TAXI_TARIFF_CASES)
    def test_tariff_tooltip_appears(self, taxi_form_opened, taxi_page,
                                    tariff_name, _expected):
        taxi_page.select_tariff(tariff_name)
        taxi_page.hover_tariff_info(tariff_name)

        assert taxi_page.is_tooltip_visible(tariff_name)

    @allure.title("Описание активного тарифа '{tariff_name}' в тултипе соответствует ТЗ")
    @pytest.mark.parametrize("tariff_name, expected_description", TAXI_TARIFF_MATCH_CASES)
    def test_tariff_tooltip_matches_tz(self, taxi_form_opened, taxi_page,
                                       tariff_name, expected_description):
        taxi_page.select_tariff(tariff_name)
        taxi_page.hover_tariff_info(tariff_name)

        assert taxi_page.is_tooltip_visible(tariff_name)
        assert expected_description in taxi_page.get_tooltip_text(tariff_name)

    @allure.title("Под тарифами отображаются поля формы заказа")
    def test_form_fields_visible(self, taxi_form_opened, taxi_page):
        assert taxi_page.is_phone_visible()
        assert taxi_page.is_payment_visible()
        assert taxi_page.is_comment_visible()
        assert taxi_page.is_requirements_visible()

        