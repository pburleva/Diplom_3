import allure
import data
from pages.reset_password_page import ResetPasswordPage
from pages.login_page import LoginPage
import urls


class TestResetPassword:

    @allure.title('Переход на страницу forgot-password по кнопке «Восстановить пароль»')
    @allure.description('Проверяем что происходит редирект на страницу forgot-password по клику '
                        'на кнопку "Восстановить Пароль"')
    def test_redirect_after_reset_password_button_click_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_reset_password_click()
        reset_password_page = ResetPasswordPage(driver)
        assert reset_password_page.get_current_url() == urls.FORGOT_PASSWORD_URL

    @allure.title('Ввод почты и клик по кнопке «Восстановить» ведет на страницу reset-password')
    @allure.description('Редирект на страницу reset-password после ввода email и нажатия кнопки "Восстановить"')
    def test_redirect_after_filling_email_and_reset_password_button_click_successful(self, driver):
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.open_page(urls.FORGOT_PASSWORD_URL)
        reset_password_page.fill_email_field(data.EXISTING_USER)
        reset_password_page.reset_password_button_click()
        reset_password_page.wait_save_button_clickable()
        assert reset_password_page.get_current_url() == urls.RESET_PASSWORD_URL

    @allure.title('клик по кнопке показать пароль делает поле активным — подсвечивает его')
    @allure.description('Проверка, что клик по иконке глаза ведет к подсвечиванию поля')
    def test_is_password_field_focused_after_eye_click_successful(self, driver):
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.open_page(urls.FORGOT_PASSWORD_URL)
        reset_password_page.fill_email_field(data.EXISTING_USER)
        reset_password_page.reset_password_button_click()
        reset_password_page.eye_icon_click()
        is_focused = reset_password_page.check_eye_class_name()
        assert is_focused == True
