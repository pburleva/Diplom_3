import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем вкладку Конструктор')
    def constructor_tab_click(self):
        self.wait_element_is_clickable(MainPageLocators.constructor_tab)
        self.click_element(MainPageLocators.constructor_tab)

    @allure.step('Кликаем вкладку Лента Заказов')
    def orders_tab_click(self):
        self.wait_element_is_clickable(MainPageLocators.orders_tab)
        self.click_element(MainPageLocators.orders_tab)

    @allure.step('Кликаем вкладку Личный кабинет')
    def personal_cabinet_tab_click(self):
        self.wait_element_is_clickable(MainPageLocators.personal_cabinet_tab)
        self.click_element(MainPageLocators.personal_cabinet_tab)

    @allure.step('Кликаем кнопку Оформить заказ')
    def create_order_button_click(self):
        self.wait_element_is_clickable(MainPageLocators.order_button)
        self.click_element(MainPageLocators.order_button)

    @allure.step('Кликаем на ингридиент')
    def ingredient_click(self):
        self.wait_element_is_clickable(MainPageLocators.ingredient)
        self.click_element(MainPageLocators.ingredient)

    @allure.step('Кликаем на крестик попапа деталей ингридиента')
    def ingredient_popup_cross_button_click(self):
        self.wait_element_is_clickable(MainPageLocators.cross_button)
        self.click_element(MainPageLocators.cross_button)

    @allure.step('Добавляем булку в бургер')
    def add_bun(self, driver):
        element_locator = MainPageLocators.bun
        target_locator = MainPageLocators.burger_basket
        self.run_action_chains(driver, element_locator, target_locator)

    @allure.step('Добавляем ингредиент в бургер')
    def add_ingredient(self, driver):
        element_locator = MainPageLocators.ingredient
        target_locator = MainPageLocators.burger_basket
        self.run_action_chains(driver, element_locator, target_locator)

    @allure.step('Добавляем необходимое количество ингредиентов')
    def add_some_ingredients(self, driver, count_ingredients):
        for ingredients in range(count_ingredients):
            self.add_ingredient(driver)

    @allure.step('Ожидаем пока 9999 изменится на номер заказа')
    def wait_default_number_invisibility(self):
        self.wait_element_invisibility(MainPageLocators.default_order_number)

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        order_number = str(self.get_element_text(MainPageLocators.order_number))
        return order_number

    @allure.step('Получаем количество добавленных ингредиентов')
    def get_ingredients_count(self):
        ingredients_count = self.get_element_text(MainPageLocators.ingredints_count)
        return ingredients_count

    @allure.step('Создаем бургер и жмем "Оформить заказ"')
    def create_burger(self, driver):
        self.constructor_tab_click()
        self.add_bun(driver)
        self.add_ingredient(driver)
        self.create_order_button_click()
        self.wait_default_number_invisibility()
        order_number = self.get_order_number()
        self.ingredient_popup_cross_button_click()
        return order_number

    @allure.step('Ожидаем пока кнопка Order будет кликабельна')
    def wait_order_button_is_clickable(self):
        self.wait_element_is_clickable(MainPageLocators.order_button)

    @allure.step('Ожидаем пока вкладка "Лента Заказов" будет кликабельна')
    def wait_orders_tab_is_clickable(self):
        self.wait_element_is_clickable(MainPageLocators.orders_tab)

    @allure.step('Ожидаем пока попап с деталями ингридиентов будет кликабелен')
    def wait_ingredient_details_popup_is_clickable(self):
        self.wait_element_is_clickable(MainPageLocators.ingredient_details_popup_text)

    @allure.step('Находим попап с деталями ингридиентов')
    def find_ingredient_details_popup(self):
        return self.find_element(MainPageLocators.ingredient_details_popup_text)

    @allure.step('Находим заголовок "Соберите бургер"')
    def find_create_burger_title(self):
        return self.find_element(MainPageLocators.create_burger_header)

    @allure.step('Находим попап "Ваш заказ начали готовить"')
    def find_order_popup(self):
        return self.find_element(MainPageLocators.order_popup)

    @allure.step('Находим текст "Ваш заказ начали готовить"')
    def find_order_popup_text_order_started_to_cook(self):
        return self.find_element(MainPageLocators.order_preparation_is_started)

    @allure.step('Ожидаем текст "Ваш заказ начали готовить"')
    def wait_order_popup_text_order_started_to_cook_is_visible(self):
        self.wait_element_is_visible(MainPageLocators.order_preparation_is_started)
