from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")
    button_name = driver.find_element("id", "newButtonName").send_keys("SkyPro")
    confirm_button_name = driver.find_element("id", "updatingButton").click()
    new_button_name = driver.find_element("id", "updatingButton").text
    
    print(new_button_name)
    
except Exception as ex:
    print(ex)
finally:
    driver.quit