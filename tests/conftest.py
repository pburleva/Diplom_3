import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FS
from webdriver_manager.firefox import GeckoDriverManager

DRIVER_PATH_CHROME = './chromedriver'
DRIVER_PATH_FIREFOX = './geckodriver'


@pytest.fixture(params=['firefox', 'chrome'], scope='function')
def driver(request):
    driver = None
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(2048, 1280)
    yield driver
    driver.quit()
