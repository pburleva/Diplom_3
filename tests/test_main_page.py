import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from locators.orders_page_locators import OrdersPageLocators
from locators.main_page_locators import MainPageLocators
import urls
import data


class TestMainFunctionality:
    @allure.title('Проверка перехода на страницу Конструктор ')
    @allure.description('Проверяем что происходит редирект на страницу https://stellarburgers.nomoreparties.site/ '
                        'по клику на вкладку Конструктор')
    def test_redirect_after_constructor_tab_click_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        main_page = MainPage(driver)
        main_page.personal_cabinet_tab_click()
        main_page.constructor_tab_click()
        main_page.wait_element_is_clickable(MainPageLocators.order_button)
        assert main_page.get_current_url() == urls.MAIN_PAGE_CONSTRUCTOR_URL

    @allure.title('Проверка перехода на страницу Лента заказов')
    @allure.description(
        'Проверяем что происходит редирект на страницу feed по клику на вкладку Лента заказов')
    def test_redirect_after_personal_cabinet_tab_click_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        login_page.wait_element_is_clickable(MainPageLocators.order_button)
        main_page = MainPage(driver)
        main_page.orders_tab_click()
        main_page.wait_element_is_clickable(OrdersPageLocators.orders_header)
        assert main_page.get_current_url() == urls.ORDERS_PAGE_URL

    @allure.title('При клике на ингридиент появится всплывающее окно с деталями')
    @allure.description('Проверяем что открывается попап при клике на ингридиент')
    def test_popup_after_ingredient_click_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        login_page.wait_element_is_clickable(MainPageLocators.order_button)
        main_page = MainPage(driver)
        main_page.ingredient_click()
        main_page.wait_element_is_clickable(MainPageLocators.ingredient_details_popup_text)
        assert main_page.find_element(MainPageLocators.ingredient_details_popup_text)

    @allure.title('При клике на крестик всплывающее окно с деталями закрывается')
    @allure.description('Проверяем что закрывается попап при клике на крестик')
    def test_popup_after_ingredient_click_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        login_page.wait_element_is_clickable(MainPageLocators.order_button)
        main_page = MainPage(driver)
        main_page.ingredient_click()
        main_page.wait_element_is_clickable(MainPageLocators.ingredient_details_popup_text)
        main_page.ingredient_popup_cross_button_click()
        assert main_page.find_element(MainPageLocators.create_burger_header)

    @allure.title('При добавлении ингридиента счетчик увеличивается')
    @allure.description('Проверяем что закрывается попап при клике на крестик')
    def test_popup_after_ingredient_adding_counter_increased_successful(self, driver, count=2):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        login_page.wait_element_is_clickable(MainPageLocators.order_button)
        main_page = MainPage(driver)
        main_page.add_some_ingredients(driver, count)
        result = main_page.get_ingredients_count()
        assert result == str(count)

    @allure.title('Оформление заказа залогиненным пользователем')
    @allure.description('Проверяем что залогиненный пользователь может оформить заказ')
    def test_order_creation_by_logged_in_user_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        login_page.wait_element_is_clickable(MainPageLocators.order_button)
        main_page = MainPage(driver)
        main_page.add_bun(driver)
        main_page.add_ingredient(driver)
        main_page.create_order_button_click()
        main_page.wait_element_is_visible(MainPageLocators.order_preparation_is_started)
        assert main_page.find_element(MainPageLocators.order_preparation_is_started)
