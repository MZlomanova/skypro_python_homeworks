from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()
chrome.get("http://uitestingplayground.com/classattr")

for _ in range(3):
    blue_button = chrome.find_element(
        "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), 'btn-primary ')]")
    blue_button.click()
    sleep(2)

    chrome.switch_to.alert.accept()
    
chrome.quit()
