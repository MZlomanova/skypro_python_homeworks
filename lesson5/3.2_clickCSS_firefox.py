from selenium import webdriver
from time import sleep

firefox = webdriver.Firefox()
try:
    firefox.get("http://uitestingplayground.com/classattr")
    for _ in range(3):
        blue_button = firefox.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), 'btn-primary ')]")
        blue_button.click()
        sleep(2)
    

        firefox.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    firefox.quit()
