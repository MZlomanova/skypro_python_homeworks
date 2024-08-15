from selenium import webdriver
from time import sleep

firefox = webdriver.Firefox()

count = 0
firefox.get("http://uitestingplayground.com/dynamicid")
blue_button = firefox.find_element(
    "xpath", '//button[text()="Button with Dynamic ID"]').click()

for _ in range(3):
    blue_button = firefox.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click
    count = count +1
    sleep(2)
    print(count)

firefox.quit()