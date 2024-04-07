from selenium.webdriver.common.by import By


class LoginPageLocators:
    reset_password_button = By.XPATH, ".//a[text()='Восстановить пароль']"
    email_field = By.XPATH, './/input[@name="name"]'
    password_field = By.XPATH, './/input[@name="Пароль"]'
    login_button = By.XPATH, './/button[text()="Войти"]'
