from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_calculator(chrome_browser: WebDriver):
    chrome_browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    chrome_browser.find_element(By.CSS_SELECTOR, "#delay").clear()
    chrome_browser.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    chrome_browser.find_element(By.XPATH, "//span[text() = '7']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '+']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '8']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '=']").click()

    WebDriverWait(chrome_browser, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text
    assert result_text == "15"
