import time

import pytest
from pages.page_add_to_cart import PageAddToCart

class TestUpdateCartQuantity:

    def test_update_cart_quantity(self, driver):
        driver.get("https://demo.nopcommerce.com/")
        driver.maximize_window()
        page = PageAddToCart(driver)


        page.scroll_to_featured_products()
        page.open_build_your_own_computer()
        page.select_processor("2.2 GHz Intel Pentium Dual-Core E2200")
        page.select_ram("2 GB")
        page.select_hdd_400gb()
        #page.select_os()
        page.update_software_options()
        page.click_add_to_cart_req_attributes()
        time.sleep(2)


        page.open_cart()


        page.update_cart_quantity(3)



