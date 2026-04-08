from selenium.webdriver.common.by import By

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    product_titles = (By.CSS_SELECTOR, ".product-title a")
    no_results_message = (By.CSS_SELECTOR, "div.no-result")

    def get_products_list(self):
        return self.driver.find_elements(*self.product_titles)

    def is_product_present(self, product_name):
        products = self.get_products_list()
        return any(product.text.strip() == product_name for product in products)

    def are_only_relevant_products_listed(self, expected_name):
        products = self.get_products_list()
        return all(expected_name in product.text for product in products)