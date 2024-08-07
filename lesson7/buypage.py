from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep

class SouseStore:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        driver.get("https://www.saucedemo.com/")
        
    def auth(self):
        self._driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self._driver.find_element(By.ID, "password").send_keys("secret_sauce")
        sleep(1)
        self._driver.find_element(By.ID, "login-button").click()
    def add_to_cart(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        
    def checkout(self):
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self._driver.find_element(By.ID, "checkout").click()
        
    def personal_data(self):
        self._driver.find_element(By.ID, "first-name").send_keys("Марина")
        self._driver.find_element(By.ID, "last-name").send_keys("Зломанова")
        self._driver.find_element(By.ID, "postal-code").send_keys("80361")
        self._driver.find_element(By.ID, "continue").click()
        
    def get_total(self):
        total = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return total
        