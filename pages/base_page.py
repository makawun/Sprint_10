from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def js_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        return self.find(locator).text

    def type_text_and_enter(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)

    def pause(self, seconds):
        ActionChains(self.driver).pause(seconds).perform()

    def hover(self, locator, pause=0.5):
        element = self.find(locator)
        ActionChains(self.driver) \
            .move_to_element(element) \
            .pause(pause) \
            .perform()

    def wait_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_presence(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_text_not_empty(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator).text.strip() != ""
        )

    def is_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_gone(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def take_screenshot(self):
        return self.driver.get_screenshot_as_png()

    