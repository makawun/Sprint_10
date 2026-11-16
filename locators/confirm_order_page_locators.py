from selenium.webdriver.common.by import By


class ConfirmOrderPageLocators:
    HEADER = (By.XPATH, ".//div[contains(@class,'order-header-title')]")

    CONFIRM_HEADER = (
        By.XPATH,
        ".//div[contains(@class,'order-header-title')]"
        "[contains(., 'мин') or contains(., 'приедет')]"
    )

    AUTOMOBILE_NUMBER = (By.XPATH, ".//div[@class='number']")
    AUTOMOBILE_IMG = (By.XPATH, ".//div[@class='order-number']/img[@alt='Car']")

    RATE = (By.XPATH, ".//div[@class='order-btn-rating']")
    DRIVER_IMG = (
        By.XPATH,
        ".//div[@class='order-btn-group']"
        "[.//div[@class='order-btn-rating']]//img"
    )
    DRIVER_NAME = (
        By.XPATH,
        ".//div[@class='order-btn-group']"
        "[.//div[@class='order-btn-rating']]/div[2]"
    )

    CANCEL_BUTTON = (
        By.XPATH,
        ".//div[@class='order-btn-group'][.//div[text()='Отменить']]/button"
    )
    DETAILS_BUTTON = (
        By.XPATH,
        ".//div[@class='order-btn-group'][.//div[text()='Детали']]/button"
    )

    DETAILS_BLOCK = (By.XPATH, ".//div[contains(@class,'order-details')]")

    PRICE = (By.XPATH, ".//div[contains(text(),'Стоимость')]")

    