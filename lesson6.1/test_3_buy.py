from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_calculator(chrome_browser: WebDriver):
    chrome_browser.get("https://www.saucedemo.com")

    chrome_browser.find_element(By.ID, "user-name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome_browser.find_element(By.ID, "login-button").click()

    chrome_browser.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack").click()
    chrome_browser.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    chrome_browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    chrome_browser.find_element(By.ID, "checkout").click()

    chrome_browser.find_element(By.ID, "first-name").send_keys("Марина")
    chrome_browser.find_element(By.ID, "last-name").send_keys("Зломанова")
    chrome_browser.find_element(By.ID, "postal-code").send_keys("80361")
    chrome_browser.find_element(By.ID, "continue").click()

    total = chrome_browser.find_element(
        By.CLASS_NAME, "summary_total_label").text
    assert total == "Total: $58.29"
