from selenium.webdriver.common.by import By


class TaxiPageLocators:
    TCARD = (By.XPATH, ".//div[@class='tariff-cards']/div")

    TCARD_WORK = (
        By.XPATH, ".//div[@class='tariff-cards']/div[contains(@class,'active')]"
    )

    TARIFF_CARD = (
        By.XPATH,
        ".//div[@class='tariff-cards']/div"
        "[.//div[@class='tcard-title'][text()='{tariff_name}']]"
    )
    
    ACTIVE_TARIFF_CARD = (
        By.XPATH,
        ".//div[@class='tariff-cards']/div[contains(@class,'active')]"
        "[.//div[@class='tcard-title'][text()='{tariff_name}']]"
    )

    INFORMATION_BUTTON = (
        By.XPATH,
        ".//div[@class='tariff-cards']/div"
        "[.//div[@class='tcard-title'][text()='{tariff_name}']]"
        "/button[contains(@class,'tcard-i')]"
    )

    TOOLTIP = (
        By.XPATH,
        ".//div[@class='tariff-cards']/div"
        "[.//div[@class='tcard-title'][text()='{tariff_name}']]"
        "//div[@data-id='tooltip']"
    )

    TARIFF_PRICE = (
        By.XPATH,
        ".//div[@class='tariff-cards']/div"
        "[.//div[@class='tcard-title'][text()='{tariff_name}']]"
        "//div[@class='tcard-price']"
    )

    PHONE_NUMBER = (By.XPATH, ".//div[@class='np-text']")
    PAYMENT = (By.XPATH, ".//div[@class='pp-text']")
    COMMENT = (By.XPATH, ".//input[@id='comment']")
    REQUIREMENTS = (By.XPATH, ".//div[@class='reqs-head']")
    ORDER_BUTTON = (By.XPATH, ".//button[@class='smart-button']")
    LAPTOP_TABLE = (By.XPATH, ".//input[@class='switch-input']")

    

