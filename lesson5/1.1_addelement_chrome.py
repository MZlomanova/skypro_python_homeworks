from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep

chrome = webdriver.Chrome()

chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")

#добавление элемента 5 раз

for _ in range(5):
    add_button = chrome.find_element(
        By.XPATH, '//button[text()="Add Element"]').click()
    sleep(1)
    
#список кнопок delete

chrome_delete_buttons = chrome.find_elements(
    "xpath", '//button[text()="Delete"]')


print(f"Размер списка кнопок Delete в Chrome:{len(chrome_delete_buttons)}")

chrome.quit()