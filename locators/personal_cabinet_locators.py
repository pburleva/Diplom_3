from selenium.webdriver.common.by import By


class PersonalCabinetPageLocators:
    profile = By.XPATH, './/a[text()="Профиль"]'
    history = By.XPATH, './/a[text()="История заказов"]'
    logout = By.XPATH, './/button[text()="Выход"]'
