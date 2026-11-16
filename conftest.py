import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

            