from selenium.webdriver.common.by import By

class WishlistPage:
    wishlist_link_xpath = "//a[@href='/wishlist']"
    add_to_wishlist_button_xpath = "//*[@id='main']/div/section/div/div/section[2]/div/div[2]/article/div[2]/div[3]/div[2]/button[3]"
    to_add_product_to_wishlist_id = "add-to-wishlist-button-4"
    add_to_cart_xpath="//*[@name='addtocartbutton']"
    select_the_checkbox_xpath = "//*[@type='checkbox' and @name='addtocart']"
    to_click_wishlist_xpath = "//*[@href='/wishlist' and @class='ico-wishlist']"
    shopping_cart_title_xpath = "//*[@class='page-title']//*[text()='Shopping cart']"

    def __init__(self, driver):
        self.driver = driver


    def add_product_to_wishlist_for_navigate(self):
        self.driver.find_element(By.XPATH, self.add_to_wishlist_button_xpath).click()

    def add_product_to_wishlist(self):
        self.driver.find_element(By.ID, self.to_add_product_to_wishlist_id).click()

    def click_wishlist(self):
        self.driver.find_element(By.XPATH, self.to_click_wishlist_xpath).click()

    def select_all_items_and_add_to_cart(self):
        checkbox = self.driver.find_element(By.XPATH, self.select_the_checkbox_xpath)
        checkbox.click()

    def click_add_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_xpath).click()

    def verify_shopping_cart_page(self):
        return self.driver.find_element(By.XPATH, self.shopping_cart_title_xpath).is_displayed()