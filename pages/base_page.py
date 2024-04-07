import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть {url} страницы")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Клик по элементу {locator}')
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step('Получить элемент {locator}')
    def find_element(self, locator):
        element = self.wait_element_is_visible(locator)
        return self.driver.find_element(*locator)

    @allure.step('Получить элемент {locator} со скроллом')
    def find_element_with_scroll(self, locator):
        element = self.wait_element_is_visible(locator)
        self.scroll_to_element(element)
        return self.driver.find_element(*locator)

    @allure.step('Скролл к элементу {element}')
    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ввести текст {text}')
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step('Подождать элемент {locator}')
    def wait_element_is_visible(self, locator):
        return WebDriverWait(self.driver, 70).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Подождать пока элемент станет кликабельным {locator}')
    def wait_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 70).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Получаем название класса для проверки активности поля')
    def get_class_name(self, locator):
        return self.wait_element_is_visible(locator).get_attribute("class")

    @allure.step('Добавляем составляющую в бургер')
    def run_action_chains(self, driver, element_locator, target_locator):
        action_chains = ActionChains(driver)
        element = self.find_element_with_scroll(element_locator)
        target = self.find_element_with_scroll(target_locator)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step('Ждем когда элемент будет спрятан {locator}')
    def wait_element_invisibility(self, locator):
        return WebDriverWait(self.driver, 40).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Получаем текст элемента {locator}')
    def get_element_text(self, locator):
        return self.find_element_with_scroll(locator).text

    '''
    @allure.step('Wait element and click {locator}')
    def wait_element_is_visible_and_click(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        element = self.find_element(locator)
        element.click()

    

    @allure.step('Get Current URL')
    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def switch_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def scroll_to_body(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
'''
