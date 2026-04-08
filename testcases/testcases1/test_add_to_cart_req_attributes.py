
import time

import pytest
from pages.page1.page_add_to_cart import PageAddToCart

class TestAddComputerWithAttributes:

    def test_add_computer_with_required_attributes(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        driver.maximize_window()
        page = PageAddToCart(driver)

        # Step 1: Scroll to Featured Products
        section = page.scroll_to_featured_products()
        assert section.is_displayed(), "Featured products section not visible"

        # Step 2: Open product
        page.open_build_your_own_computer()

        # Step 3: Try to add without attributes
        page.click_add_to_cart_without_attributes()
        time.sleep(4)

        # Step 4: Verify error message
        # error_msg = page.get_error_message()
        # assert "Please select RAM" in error_msg
        # page.close_error_message()

        # Step 5: Select attributes
        page.select_processor("2.2 GHz Intel Pentium Dual-Core E2200")
        page.select_ram("2 GB")
        page.select_hdd_400gb()
        page.update_software_options()

        # Step 6: Add to cart
        page.click_add_to_cart_req_attributes()

        # Verify success message
        assert page.verify_product_added_message()

        # Close the message
        page.close_green_message()

        time.sleep(5)



        # Step 8: Verify product in cart
        page.open_cart()
        assert page.get_cart_quantity() == "(1)", "Cart quantity is not 1"
        assert page.get_cart_sku() == "COMP_CUST", "SKU mismatch"
        assert page.get_cart_product_name() == "Build your own computer", "Product name mismatch"
        print("verified")
