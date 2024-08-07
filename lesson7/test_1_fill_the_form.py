from fillformpage import *

def test_fill_form(chrome_browser: WebDriver):
    main_page = FillFormPage(chrome_browser)
    main_page.submit_form()

    assert "alert-danger" in main_page.get_zip_code_element().get_attribute("class")
    assert "success" in main_page.get_phone_element().get_attribute("class")
    assert "success" in main_page.get_address_element().get_attribute("class")
    assert "success" in main_page.get_company_element().get_attribute("class")
    assert "success" in main_page.get_country_element().get_attribute("class")
    assert "success" in main_page.get_e_mail_element().get_attribute("class")
    assert "success" in main_page.get_first_name_element().get_attribute("class")
    assert "success" in main_page.get_last_name_element().get_attribute("class")
    assert "success" in main_page.get_job_position_element().get_attribute("class")
    assert "success" in main_page.get_city_element().get_attribute("class")
