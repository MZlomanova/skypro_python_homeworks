from selenium.webdriver.chrome.webdriver import WebDriver
from calculatorpage import *

def test_calculator(chrome_browser: WebDriver):
    #открыть браузер (создаем page object)
    calc_page = CalculatorPage(chrome_browser)
    #заполняем поля
    calc_page.fill_delay_field()
    #жмем на кнопку
    calc_page.push_the_buttons()
    #получаем результат  
    result_text = calc_page.get_result()
    #сравниваем результат  
    assert result_text == "15"
