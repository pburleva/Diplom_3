import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_cabinet_page import PersonalCabinetPage
import urls
import data


class TestPersonalCabinet:

    @allure.title('Проверка перехода на страницу Личный кабинет')
    @allure.description('Проверяем что происходит редирект на страницу account/profile'
                        ' по клику на вкладку Личный кабинет')
    def test_redirect_after_personal_cabinet_tab_click_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        main_page = MainPage(driver)
        main_page.personal_cabinet_tab_click()
        personal_cabinet_page = PersonalCabinetPage(driver)
        personal_cabinet_page.wait_profile_is_visible()
        assert personal_cabinet_page.get_current_url() == urls.PERSONAL_CABINET_PROFILE_URL

    @allure.title('Проверка перехода на страницу История заказов')
    @allure.description('Проверяем что происходит редирект на страницу order-history'
                        ' по клику на вкладку История заказов')
    def test_redirect_after_personal_cabinet_history_of_orders_tab_click_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        main_page = MainPage(driver)
        main_page.personal_cabinet_tab_click()
        personal_cabinet_page = PersonalCabinetPage(driver)
        personal_cabinet_page.history_item_click()
        assert personal_cabinet_page.get_current_url() == urls.PERSONAL_CABINET_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта по клику на Выход')
    @allure.description('Проверяем что происходит выход из аккаунта'
                        ' по клику на вкладку Выход')
    def test_redirect_after_personal_cabinet_logout_tab_click_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        main_page = MainPage(driver)
        main_page.personal_cabinet_tab_click()
        personal_cabinet_page = PersonalCabinetPage(driver)
        personal_cabinet_page.logout_item_click()
        login_page.wait_login_button_clickable()
        assert personal_cabinet_page.get_current_url() == urls.LOGIN_URL
