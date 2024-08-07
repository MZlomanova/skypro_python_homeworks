from selenium.webdriver.chrome.webdriver import WebDriver
from forfillform import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    #открываем страницу
    def __init__(self, driver: WebDriver):
        self._driver = driver
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    #заполняем поля
    def fill_delay_field(self):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    #жмем на кнопки с циферками и равно    
    def push_the_buttons(self):
        self._driver.find_element(By.XPATH, "//span[text() = '7']").click()
        self._driver.find_element(By.XPATH, "//span[text() = '+']").click()
        self._driver.find_element(By.XPATH, "//span[text() = '8']").click()
        self._driver.find_element(By.XPATH, "//span[text() = '=']").click()

    #отображение результата
    def get_result(self):
        
        WebDriverWait(self._driver, 50).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        result_text = self._driver.find_element(By.CLASS_NAME, "screen").text
        return result_text
