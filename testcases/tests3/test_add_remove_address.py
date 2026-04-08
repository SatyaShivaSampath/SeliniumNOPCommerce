import pytest
from pages.pages3.login_page import LoginPage
from pages.pages3.address_page import AddressPage

@pytest.mark.order(8)
@pytest.mark.smoke
@pytest.mark.positive
def test_add_new_address(driver):
    driver.get("https://demo.nopcommerce.com/")
    login_page = LoginPage(driver)
    address_page = AddressPage(driver)
    
    assert "nopCommerce demo store" in driver.title
    
    login_page.login("abcde.fghi@gmail.com","AbcdeFghi_1234")
    
    address_page.navigate_to_address()

    address_page.add_new_address(
        fname="demo",
        lname="example",
        email="demo@example.com",
        company="Cognizant",
        country="India",
        state="Tamil Nadu",
        city="Coimbatore",
        address1="123 Main Street",
        zip_code="641001",
        phone="9876543210"
    )
    assert address_page.verify_address_added("demo example")


@pytest.mark.order(9)
def test_remove_address(driver):
    driver.get("https://demo.nopcommerce.com/")
    login_page = LoginPage(driver)
    address_page = AddressPage(driver)
    
    login_page.login("abcde.fghi@gmail.com","AbcdeFghi_1234")
    address_page.navigate_to_address()
    
    address_page.remove_address()
    
    assert address_page.verify_address_removed("demo example")












