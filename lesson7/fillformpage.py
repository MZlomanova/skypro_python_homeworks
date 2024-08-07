from selenium.webdriver.chrome.webdriver import WebDriver
from forfillform import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FillFormPage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def submit_form(self):
        self._driver.find_element(By.NAME, "first-name").send_keys(first_name)
        self._driver.find_element(By.NAME, "last-name").send_keys(last_name)
        self._driver.find_element(By.NAME, "address").send_keys(address)
        self._driver.find_element(By.NAME, "e-mail").send_keys(email)
        self._driver.find_element(By.NAME, "phone").send_keys(phone_number)
        self._driver.find_element(By.NAME, "zip-code").send_keys(zip_code)
        self._driver.find_element(By.NAME, "city").send_keys(city)
        self._driver.find_element(By.NAME, "country").send_keys(country)
        self._driver.find_element(By.NAME, "job-position").send_keys(job_position)
        self._driver.find_element(By.NAME, "company").send_keys(company)
        WebDriverWait(self._driver, 50, 3).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    
    def get_zip_code_element(self):
        return self._driver.find_element(By.ID, "zip-code")

    def get_first_name_element(self):
        return self._driver.find_element(By.ID, "first-name")

    def get_last_name_element(self):
        return self._driver.find_element(By.ID, "last-name")

    def get_address_element(self):
        return self._driver.find_element(By.ID, "address")

    def get_e_mail_element(self):
        return self._driver.find_element(By.ID, "e-mail")

    def get_phone_element(self):
        return self._driver.find_element(By.ID, "phone")

    def get_city_element(self):
        return self._driver.find_element(By.ID, "city")

    def get_country_element(self):
        return self._driver.find_element(By.ID, "country")

    def get_job_position_element(self):
        return self._driver.find_element(By.ID, "job-position")

    def get_company_element(self):
        return self._driver.find_element(By.ID, "company")
