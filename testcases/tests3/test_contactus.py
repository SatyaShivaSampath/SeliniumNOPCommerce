import pytest
from selenium.webdriver.common.by import By
from pages.pages3.contact_page import ContactPage

@pytest.mark.order(5)
@pytest.mark.regression
@pytest.mark.positive
def test_contact_us_form(driver):
    driver.get("https://demo.nopcommerce.com/")
    contact_page = ContactPage(driver)
    contact_page.submit_enquiry("Demo User","demo@example.com","This is a test enquiry.")
    assert "successfully sent" in contact_page.get_success_message()















