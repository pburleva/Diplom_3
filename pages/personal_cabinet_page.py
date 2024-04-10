import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.personal_cabinet_locators import PersonalCabinetPageLocators


class PersonalCabinetPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем вкладку Личный кабинет')
    def personal_cabinet_tab_click(self):
        self.wait_element_is_clickable(MainPageLocators.personal_cabinet_tab)
        self.click_element(MainPageLocators.personal_cabinet_tab)

    @allure.step('Кликаем пункт История заказов')
    def history_item_click(self):
        self.wait_element_is_clickable(PersonalCabinetPageLocators.history)
        self.click_element(PersonalCabinetPageLocators.history)

    @allure.step('Кликаем пункт Выход')
    def logout_item_click(self):
        self.wait_element_is_clickable(PersonalCabinetPageLocators.logout)
        self.click_element(PersonalCabinetPageLocators.logout)

    @allure.step('Ожидаем пока текст Профиль будет видим')
    def wait_profile_is_visible(self):
        self.wait_element_is_visible(PersonalCabinetPageLocators.profile)
