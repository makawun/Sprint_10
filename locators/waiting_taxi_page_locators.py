from selenium.webdriver.common.by import By

class WaitingTaxiPageLocators:

    HEADER = (By.XPATH, ".//div[@class='order-header-title']")

    TIMER = (By.XPATH, ".//div[@class='order-header-time']")

    CANCEL_BUTTON = (By.XPATH, ".//img[@alt='close']/..")

    DETAILS_BUTTON = (By.XPATH, ".//img[@alt='burger']/..")