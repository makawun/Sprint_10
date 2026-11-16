from selenium.webdriver.common.by import By

class MainPageLocators:
    
    FROM_INPUT = (By.XPATH, ".//input[@id='from']")

    TO_INPUT = (By.XPATH, ".//input[@id='to']")