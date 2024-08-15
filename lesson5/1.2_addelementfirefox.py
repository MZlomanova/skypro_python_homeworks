from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep

firefox = webdriver.Firefox()

firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

#добавление элемента 5 раз

for _ in range(5):
    add_button = firefox.find_element(
        By.XPATH, '//button[text()="Add Element"]').click()
    sleep(1)
    
#список кнопок delete

firefox_delete_buttons = firefox.find_elements(
    "xpath", '//button[text()="Delete"]')


print(f"Размер списка кнопок Delete в FireFox:{len(firefox_delete_buttons)}")

firefox.quit()