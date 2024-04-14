from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    email_field = By.XPATH, '//input[@name="name"]'
    reset_password_button = By.XPATH, './/button[text()="Восстановить"]'
    save_button = By.XPATH, './/button[text()="Сохранить"]'
    password_button = By.XPATH, './/label[text()="Пароль"]'
    eye_button = By.CLASS_NAME, 'input__icon'
