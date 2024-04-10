import allure
from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем, что в классе есть подсветка')
    def check_eye_class_name(self):
        if 'input__placeholder-focused' in self.get_class_name(ResetPasswordPageLocators.password_button):
            return True
        else:
            return False

    @allure.step('Заполняем поле email')
    def fill_email_field(self, email):
        self.wait_element_is_clickable(ResetPasswordPageLocators.email_field)
        self.enter_text(ResetPasswordPageLocators.email_field, email)

    @allure.step('Кликаем кнопку восстановления пароля')
    def reset_password_button_click(self):
        self.wait_element_is_clickable(ResetPasswordPageLocators.reset_password_button)
        self.click_element(ResetPasswordPageLocators.reset_password_button)

    @allure.step('Кликаем иконку глаз в поле пароль')
    def eye_icon_click(self):
        self.wait_element_is_clickable(ResetPasswordPageLocators.eye_button)
        self.click_element(ResetPasswordPageLocators.eye_button)

    @allure.step('Ожидаем пока кнопка "Сохранить" будет кликабельна')
    def wait_save_button_clickable(self):
        self.wait_element_is_clickable(ResetPasswordPageLocators.save_button)
