import time

import pytest
from pages.page_add_to_cart import PageAddToCart

class TestPageAddToCart:

    def test_add_to_cart(self, driver):
        self.driver = driver
        driver.get("https://demo.nopcommerce.com/")
        driver.maximize_window()
        page = PageAddToCart(driver)

        # Navigate through links
        page.click_electronics_link()
        page.click_cell_phones_link()
        page.click_mobile_link()

        # Add to cart
        page.add_mobile_to_cart()


        # Verify success message
        assert page.verify_product_added_message()

        # Close the message
        #page.close_green_message()

        time.sleep(5)
        # Verify cart quantity is updated
        qty = page.get_cart_quantity()
        assert "(1)" in qty, f"Expected cart quantity (1), but got {qty}"


