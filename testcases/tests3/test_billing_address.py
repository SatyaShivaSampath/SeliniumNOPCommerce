import pytest
import time
from pages3.login_page import LoginPage
from pages3.address_page import AddressPage
from pages3.checkout_page import CheckoutPage
from pages3.product_page import ProductPage
from pages3.address_page import AddressPage

@pytest.mark.order(10)
@pytest.mark.smoke
@pytest.mark.positive
def test_billing_address_for_new_address(driver):
    driver.get("https://demo.nopcommerce.com/")
    login_page = LoginPage(driver)
    address_page = AddressPage(driver)
    checkout_page = CheckoutPage(driver)
    product_page = ProductPage(driver)

    assert "nopCommerce demo store" in driver.title

    login_page.login("abcde.fghi@gmail.com", "AbcdeFghi_1234")
    
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

    # Add product to cart
    time.sleep(3)
    product_page.add_first_product_to_cart()

    # Proceed to checkout
    checkout_page.go_to_checkout()

    if not checkout_page.is_address_present("demo example"):
        checkout_page.add_new_billing_address(
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

    address_page.navigate_to_address()
    assert address_page.verify_address_added("demo example")
