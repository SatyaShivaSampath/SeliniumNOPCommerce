import pytest
from pages.pages2.place_order_register_page import place_order_register_user
import time
from pages2.check_out_as_a_guest_page import place_order_as_a_guest_user
@pytest.mark.parametrize("firstname,lastname,email,company,password", [
    ("John", "Doe", "john.doe236@test.com", "TestCompany", "Password123"),
    ("Jane", "Smith", "jane.smith467@test.com", "AnotherCompany", "Password456"),
])
def test_place_order_register(driver, firstname, lastname, email, company, password):
    page = place_order_register_user(driver)
    page1=place_order_as_a_guest_user(driver)
    
    assert page.verify_home_page()
    time.sleep(2)
    page.add_product_to_cart_for_navigate()
    time.sleep(4)
    page.add_product_to_cart()
    time.sleep(4)
    page.click_shopping_cart()
    time.sleep(4)
    page.agree_terms()
    page.click_checkout()
    time.sleep(4)
    page.click_register_button()
    page.fill_registration_form(firstname, lastname, email, company, password)
    assert page.verify_registration_success()
    time.sleep(4)
    page.after_check_continue_button()
    time.sleep(3)
    page.to_click_i_agree()
    time.sleep(2)
    page.after_clicking_register_to_check_thecheckout()
    page1.add_address(
        fname="John",
        lname="Doe",
        email="johndoe@example.com",
        company="TestCompany",
        country="India",
        state="Andhra Pradesh",
        city="vizinagaram",
        address1="123 Test Street",
        zip_code="10001",
        phone="1234567890"
    )
    time.sleep(2)

    
    page1.click_continue_billing()
    time.sleep(2)

    
    page1.click_continue_shipping_method()
    time.sleep(2)

    
    page1.click_continue_payment_method()
    time.sleep(2)

    page1.click_continue_payment_info()
    time.sleep(2)

    page1.click_confirm_order()
    time.sleep(2)
    assert page1.to_confirm_order()

    order_number = page1.to_verify_no_of_order()
    assert order_number is not None
    print(f"Order placed successfully. Order Number: {order_number}")

