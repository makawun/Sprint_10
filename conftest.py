import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data.addresses import Addresses
from data.taxi_texts import TaxiTexts
from pages.added_address_page import AddedAddressPage
from pages.base_page import BasePage
from pages.confirm_order_page import ConfirmOrderPage
from pages.main_page import MainPage
from pages.taxi_page import TaxiPage
from pages.waiting_taxi_page import WaitingTaxiPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--headless=new")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-renderer-backgrounding")
    options.add_argument("--disable-features=CalculateNativeWinOcclusion")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open()
    return page


@pytest.fixture
def added_address_page(driver):
    return AddedAddressPage(driver)


@pytest.fixture
def taxi_page(driver):
    return TaxiPage(driver)


@pytest.fixture
def waiting_taxi_page(driver):
    return WaitingTaxiPage(driver)


@pytest.fixture
def confirm_order_page(driver):
    return ConfirmOrderPage(driver)


@pytest.fixture
def addresses_entered(main_page):
    main_page.enter_from_address(Addresses.FROM_ADDRESS)
    main_page.enter_to_address(Addresses.TO_ADDRESS)


@pytest.fixture
def same_address_entered(main_page):
    main_page.enter_from_address(Addresses.FROM_ADDRESS)
    main_page.enter_to_address(Addresses.FROM_ADDRESS)


@pytest.fixture
def taxi_form_opened(addresses_entered, added_address_page):
    added_address_page.click_fast_mode()
    added_address_page.click_call_taxi()


@pytest.fixture
def tariff_price(taxi_form_opened, taxi_page):
    return taxi_page.get_tariff_price(TaxiTexts.DEFAULT_ORDER_TARIFF)


@pytest.fixture
def order_placed(taxi_form_opened, tariff_price, taxi_page):
    taxi_page.select_tariff(TaxiTexts.DEFAULT_ORDER_TARIFF)
    taxi_page.toggle_laptop_table()
    taxi_page.click_order()


@pytest.fixture
def confirmed_order(order_placed, confirm_order_page):
    confirm_order_page.wait_confirm_header()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv:
            allure.attach(
                BasePage(drv).take_screenshot(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG,
            )

            