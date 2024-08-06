from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
input_name = driver.find_element(By.ID, "username").send_keys("tomsmith")
sleep(2)
input_password = driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(2)


button = driver.find_element(By.TAG_NAME, "button").click()
sleep(3)
    
driver.quit()