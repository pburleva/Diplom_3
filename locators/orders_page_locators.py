from selenium.webdriver.common.by import By


class OrdersPageLocators:
    orders_header = By.XPATH, ".//h1[text()='Лента заказов']"
    order_popup = By.XPATH, './/div[contains(@class,"Modal_orderBox__1xWdi")]'
    last_order_card = By.XPATH, './/ul[1]/li[1][contains(@class,"OrderHistory_listItem__2x95r mb-6")]'
    orders_done = By.XPATH, './/ul[1][contains(@class,"OrderFeed_orderList")]'

    orders_all = By.XPATH, './/div[2]/p[contains(@class,"OrderFeed_number__2MbrQ")]'
    orders_today = By.XPATH, './/div[3]/p[contains(@class,"OrderFeed_number__2MbrQ")]'
    orders_in_work = By.XPATH, './/ul[2]/li[contains(@class,"text text_type_digits-default")]'
    '''
    
    last_order = By.XPATH, './/div[contains(@class,"OrderHistory_dataBox__1mkxK")]'
    order_panel = By.XPATH, './/div[contains(@class,"Modal_orderBox__1xWdi")]'
    
    orders_done = By.XPATH, './/ul[1][contains(@class,"OrderFeed_orderList")]'
    order_compound = By.XPATH, './/div/p[3][text()="Cостав"]'
    '''