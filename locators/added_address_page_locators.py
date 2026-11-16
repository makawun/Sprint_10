from selenium.webdriver.common.by import By


class AddedAddressPageLocators:
    YMAP = (By.XPATH, ".//ymaps[contains(text(), '{address}')]")

    ROUTE_BLOCK = (By.XPATH, ".//div[@class='type-picker shown']")

    DURATION = (By.XPATH, ".//div[@class='duration']")

    RESULT_TEXT = (By.XPATH, ".//div[@class='text']")

    ACTIVE_TAB = (By.XPATH, ".//div[contains(@class,'mode') and contains(@class,'active')]")

    OPTIMUM_ROUTE_MODE = (By.XPATH, ".//div[text()='Оптимальный']")
    FAST_ROUTE_MODE = (By.XPATH, ".//div[text()='Быстрый']")
    SELF_ROUTE_MODE = (By.XPATH, ".//div[text()='Свой']")

    CAR_TYPE = (By.XPATH, ".//img[@src='/static/media/car.8a2b1ff5.svg']/..")
    WALK_TYPE = (By.XPATH, ".//img[@src='/static/media/walk.d33bf83c.svg']/..")
    TAXI_TYPE = (By.XPATH, ".//img[@src='/static/media/taxi-active.b0be3054.svg']/..")
    BIKE_TYPE = (By.XPATH, ".//img[@src='/static/media/bike.fb41c762.svg']/..")
    SCOOTER_TYPE = (By.XPATH, ".//img[@src='/static/media/scooter.cf9bb57e.svg']/..")
    DRIVE_TYPE = (By.XPATH, ".//img[@src='/static/media/drive.fa5137d7.svg']/..")

    ACTION_BUTTON = (
        By.XPATH,
        ".//div[@class='results-text']/button[contains(., '{button_text}')]"
    )