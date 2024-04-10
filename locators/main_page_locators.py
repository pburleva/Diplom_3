from selenium.webdriver.common.by import By


class MainPageLocators:
    personal_cabinet_tab = By.XPATH, './/p[text()="Личный Кабинет"]'
    constructor_tab = By.XPATH, './/p[text()="Конструктор"]'
    orders_tab = By.XPATH, './/p[text()="Лента Заказов"]'
    order_button = By.XPATH, './/button[text()="Оформить заказ"]'
    ingredient = By.XPATH, './/img[contains(@alt,"Соус Spicy-X")]'
    ingredient_details_popup = By.XPATH, ".//div[(@class = 'Modal_modal__contentBox__sCy8X pt-10 pb-15')]"
    ingredient_details_popup_text = By.XPATH, './/h2[text()="Детали ингредиента"]'
    cross_button = By.XPATH, './/button[@type="button"]'
    create_burger_header = By.XPATH, './/h1[text()="Соберите бургер"]'
    bun = By.XPATH, './/img[contains(@alt,"Флюоресцентная булка R2-D3")]'
    burger_basket = By.XPATH, './/ul[contains(@class,"BurgerConstructor_basket")]'
    default_order_number = By.XPATH, './/h2[text()="9999"]'
    order_number = By.XPATH, './/h2[contains(@class,"Modal_modal__title_shadow")]'
    ingredints_count = By.XPATH, './/ul[2]/a[1]/div[1]/p[contains(@class,"counter_counter")]'
    order_preparation_is_started = By.XPATH, './/p[text()="Ваш заказ начали готовить"]'
    order_popup = By.XPATH, './/div[contains(@class,"Modal_orderBox__1xWdi")]'
