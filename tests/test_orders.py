import allure
from pages.login_page import LoginPage
from pages.orders_page import OrdersPage
from pages.personal_cabinet_page import PersonalCabinetPage
from pages.main_page import MainPage
from locators.login_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.orders_page_locators import OrdersPageLocators
from locators.personal_cabinet_locators import PersonalCabinetPageLocators
import urls
import data


class TestOrders:
    @allure.title('Клик на заказ, открывает окно с деталями')
    @allure.description('')
    def test_order_click_leads_to_details_popup_opening_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        login_page.wait_element_is_clickable(MainPageLocators.order_button)
        main_page = MainPage(driver)
        main_page.orders_tab_click()
        orders_page = OrdersPage(driver)
        orders_page.last_order_card_click()
        assert main_page.find_element(OrdersPageLocators.order_popup)

    @allure.title('Заказы пользователя отображаются на странице Лента заказов')
    @allure.description('заказы пользователя из раздела История заказов отображаются на странице Лента заказов')
    def test_users_order_in_list_of_all_orders_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        login_page.wait_element_is_clickable(MainPageLocators.order_button)
        main_page = MainPage(driver)
        order_number = main_page.create_burger(driver)
        orders_page = OrdersPage(driver)
        orders_done = orders_page.get_orders_done()
        assert order_number in orders_done

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_for_all_orders_increased_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        login_page.wait_element_is_clickable(MainPageLocators.order_button)
        main_page = MainPage(driver)
        main_page.orders_tab_click()
        orders_page = OrdersPage(driver)
        all_orders_count = orders_page.get_all_orders_count()
        main_page.create_burger(driver)
        main_page.orders_tab_click()
        all_orders_after_order = OrdersPage(driver).get_all_orders_count()
        exp_res = all_orders_count + 1
        assert all_orders_after_order == exp_res

    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_for_today_orders_increased_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        login_page.wait_element_is_clickable(MainPageLocators.order_button)
        main_page = MainPage(driver)
        main_page.orders_tab_click()
        orders_page = OrdersPage(driver)
        today_orders_count = orders_page.get_today_orders_count()
        main_page.create_burger(driver)
        main_page.orders_tab_click()
        today_orders_after_order = OrdersPage(driver).get_today_orders_count()
        exp_res = today_orders_count + 1
        assert today_orders_after_order == exp_res

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    @allure.description('после оформления заказа его номер появляется в разделе В работе')
    def test_order_is_in_in_work_orders_successful(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(urls.LOGIN_URL)
        login_page.login_by_user_successful(data.EXISTING_USER, data.PASSWORD_OF_EXISTING_USER)
        login_page.wait_element_is_clickable(MainPageLocators.order_button)
        main_page = MainPage(driver)
        order_number = main_page.create_burger(driver)
        main_page.orders_tab_click()
        orders_page = OrdersPage(driver)
        orders_in_work = orders_page.get_orders_in_work()
        assert order_number in orders_in_work
