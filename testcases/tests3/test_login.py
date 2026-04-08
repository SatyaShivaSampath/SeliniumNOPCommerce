import pytest
from selenium.webdriver.common.by import By
from pages.pages3.login_page import LoginPage

@pytest.mark.order(3)
@pytest.mark.smoke
@pytest.mark.positive
def test_login_valid_credentails(driver):
    driver.get("https://demo.nopcommerce.com/")
    login_page = LoginPage(driver)
    login_page.login("abcde.fghi@gmail.com","AbcdeFghi_1234")
    assert login_page.is_logged_in()

@pytest.mark.order(4)
@pytest.mark.regression
@pytest.mark.negative
def test_invalid_login(driver):
    driver.get("https://demo.nopcommerce.com/")
    login_page = LoginPage(driver)
    login_page.login("demo3@example.com","wrongpass")
    assert "unsuccessful" in login_page.get_error_message()














