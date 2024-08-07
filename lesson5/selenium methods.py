from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#from time import sleep
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver.get("https://ya.ru/") #открывается первая страница
driver.get("https://vk.com/") #открывается вторая страница


for x in range(1, 10):
   driver.back()
   driver.forward() 

sleep(50)