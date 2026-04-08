from selenium.webdriver.common.by import By

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver

    product_name = (By.CSS_SELECTOR, "div.product-name h1")
    short_description = (By.CSS_SELECTOR, "div.short-description")
    product_price = (By.CSS_SELECTOR, "div.product-price span")
    add_to_cart_button = (By.ID, "add-to-cart-button-4")
    full_description_tab = (By.CSS_SELECTOR, "div.full-description")
    specifications_tab = (By.CSS_SELECTOR, "div.product-specs-box")

    def get_product_name(self):
        return self.driver.find_element(*self.product_name).text

    def is_short_description_visible(self):
        return self.driver.find_element(*self.short_description).is_displayed()

    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text

    def is_add_to_cart_visible(self):
        return self.driver.find_element(*self.add_to_cart_button).is_displayed()

    def are_tabs_visible(self):
        return (self.driver.find_element(*self.full_description_tab).is_displayed() and
            self.driver.find_element(*self.specifications_tab).is_displayed())