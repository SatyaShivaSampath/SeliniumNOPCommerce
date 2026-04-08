import pytest
from pages3.login_page import LoginPage

@pytest.mark.order(6)
@pytest.mark.smoke
@pytest.mark.positive
def test_login_valid_credentials(driver):
    driver.get("https://demo.nopcommerce.com/")
    login_page = LoginPage(driver)
    login_page.login("abcd.fghi@gmail.com", "AbcdeFghi_1234")
    assert login_page.is_logged_in()    

    message = login_page.product_comparison()
    assert "You have no items to compare" in message
