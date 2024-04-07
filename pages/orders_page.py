import allure

import urls
from pages.base_page import BasePage
from locators.orders_page_locators import OrdersPageLocators


class OrdersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем карточку последнего заказа')
    def last_order_card_click(self):
        self.wait_element_is_clickable(OrdersPageLocators.last_order_card)
        self.click_element(OrdersPageLocators.last_order_card)

    @allure.step('Получаем готовые заказы')
    def get_orders_done(self):
        self.open_page(urls.ORDERS_PAGE_URL)
        orders_done = str(self.get_element_text(OrdersPageLocators.orders_done))
        return orders_done

    @allure.step('Получаем количество всех заказов')
    def get_all_orders_count(self):
        all_orders = int(self.get_element_text(OrdersPageLocators.orders_all))
        return all_orders

    @allure.step('Получаем количество сегодняшних заказов')
    def get_today_orders_count(self):
        self.open_page(urls.ORDERS_PAGE_URL)
        today_orders = int(self.get_element_text(OrdersPageLocators.orders_today))
        return today_orders

    @allure.step('Получаем заказы в работе')
    def get_orders_in_work(self):
        self.open_page(urls.ORDERS_PAGE_URL)
        orders_in_work = str(self.get_element_text(OrdersPageLocators.orders_in_work))
        return orders_in_work

