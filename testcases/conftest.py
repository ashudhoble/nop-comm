import pytest
from selenium import webdriver

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    url = 'https://admin-demo.nopcommerce.com'
    driver.get(url)
    driver.maximize_window()
    return driver
