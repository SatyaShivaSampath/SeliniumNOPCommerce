import pytest
import time
from pages.page_add_to_cart import PageAddToCart

class TestMiniCart:

    def test_mini_cart_functionality(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        driver.maximize_window()
        page = PageAddToCart(driver)

        # Step 1: Navigate to Electronics → Cell phones → Mobile
        page.click_electronics_link()
        page.click_cell_phones_link()
        page.click_mobile_link()

        # Step 2: Add mobile to cart
        page.add_mobile_to_cart()
        time.sleep(3)  # wait for success message

        page.close_green_message()

        time.sleep(3)
        # Step 3: Hover over cart
        page.hover_over_cart()
        assert page.is_mini_cart_visible(), "Mini-cart dropdown not visible"

        # Step 4: Verify product details
        name, price = page.get_mini_cart_product_details()
        print(f" Mini-cart shows product: {name}, Price: {price}")
        assert "HTC One Mini Blue" in name  # product name check


