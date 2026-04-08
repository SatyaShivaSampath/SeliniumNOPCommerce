from pages2.check_out_as_a_guest_page import place_order_as_a_guest_user
import time

def test_place_order_register(driver):
    page = place_order_as_a_guest_user(driver)
    
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
    page.click_check_out_as_guest_button()

    page.add_address(
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

    page.click_continue_billing()
    time.sleep(2)

    page.click_continue_shipping_method()
    time.sleep(2)

    page.click_continue_payment_method()
    time.sleep(2)

    page.click_continue_payment_info()
    time.sleep(2)
    page.click_confirm_order()
    time.sleep(2)
    assert page.to_confirm_order()

    order_number = page.to_verify_no_of_order()
    assert order_number is not None
    print(f"Order placed successfully. Order Number: {order_number}")
  

