from selenium.webdriver.common.by import By

class CategoryPage:
    def __init__(self, driver):
        self.driver = driver

    notebooks_link = (By.LINK_TEXT, "Notebooks")
    notebooks_heading = (By.XPATH, "//h1[text()='Notebooks']")
    product_titles = (By.CSS_SELECTOR, ".product-title a")

    def click_notebooks(self):
        self.driver.find_element(*self.notebooks_link).click()

    def is_notebooks_page_visible(self):
        return self.driver.find_element(*self.notebooks_heading).is_displayed()

    def get_products_list(self):
        return self.driver.find_elements(*self.product_titles)

    def click_product(self, product_name):
        products = self.get_products_list()
        for product in products:
            if product.text.strip() == product_name:
                product.click()
                break