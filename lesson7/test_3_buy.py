from selenium.webdriver.chrome.webdriver import WebDriver
from buypage import *

def test_buy(chrome_browser: WebDriver):
    store_page = SouseStore (chrome_browser)
    store_page.auth()
    store_page.add_to_cart()
    store_page.checkout()
    store_page.personal_data()
    result = store_page.get_total()
    assert result == "Total: $58.29"