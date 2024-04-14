from selenium.webdriver.common.by import By


class OrdersPageLocators:
    orders_header = By.XPATH, ".//h1[text()='Лента заказов']"
    order_popup = By.XPATH, './/div[contains(@class,"Modal_orderBox__1xWdi")]'
    last_order_card = By.XPATH, ('.//li[contains(@class,"OrderHistory_listItem__2x95r mb-6")]/'
                                 'a[@href="/feed/661803989ed280001b3e51ff"]')
    orders_done = By.XPATH, './/ul[@class="OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]'
    orders_all = By.XPATH, ('.//div[@class="undefined mb-15"]'
                            '/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    orders_today = By.XPATH, ('.//div[not(contains(@class, "undefined mb-15"))]/'
                              'p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    orders_in_work = By.XPATH, ('.//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/'
                                'li[@class="text text_type_digits-default mb-2"]')
