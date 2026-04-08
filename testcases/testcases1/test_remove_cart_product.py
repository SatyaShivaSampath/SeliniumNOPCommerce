import time

import pytest
from pages.pages1.page_add_to_cart import PageAddToCart

class TestRemoveCartProduct:
    def test_remove_cart_product(self, driver):

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
        time.sleep(5)


        page.open_cart()
        time.sleep(3)

        page.remove_product_from_cart()
        time.sleep(5)
        assert page.is_cart_empty(), "Cart is not empty after removing product"
        print("✅ Product removed and cart is empty")



