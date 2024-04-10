import allure
from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Логин пользователем успешный')
    def login_by_user_successful(self, login, password):
        self.wait_element_is_clickable(LoginPageLocators.email_field)
        self.wait_element_is_clickable(LoginPageLocators.password_field)
        self.wait_element_is_clickable(LoginPageLocators.login_button)
        self.enter_text(LoginPageLocators.email_field, login)
        self.enter_text(LoginPageLocators.password_field, password)
        self.click_element(LoginPageLocators.login_button)

    @allure.step('Кликаем кнопку восстановления пароля')
    def login_reset_password_click(self):
        self.wait_element_is_clickable(LoginPageLocators.reset_password_button).click()

    @allure.step('Ожидаем пока кнопка "Войти" будет кликабельна')
    def wait_login_button_clickable(self):
        self.wait_element_is_clickable(LoginPageLocators.login_button)




