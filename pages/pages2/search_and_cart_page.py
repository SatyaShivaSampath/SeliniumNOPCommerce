from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class SearchAndCartPage:
    search_input_xpath = "//input[@id='small-searchterms']"
    search_button_xpath = "//button[@type='submit' and contains(@class,'search-box-button')]"
    product_link_xpath = "//h2[@class='product-title']/a[contains(text(),'Apple MacBook Pro')]"
    add_to_cart_button_xpath = "//*[@id='add-to-cart-button-4']"
    shopping_cart_link_xpath = "//a[@class='ico-cart']"
    cart_quantity_xpath = "//span[@class='cart-qty']"
    login_link_xpath = "//a[@href='/login?returnUrl=%2Fapple-macbook-pro']"
    email_input_xpath = "//input[@id='Email']"
    password_input_xpath = "//input[@id='Password']"
    login_button_xpath = "//button[@class='button-1 login-button']"
    welcome_message_xpath = "//*[@href='/logout']"
    cart_product_name_xpath = "//a[@class='product-name']"
    cart_quantity_input_xpath = "//input[@class='qty-input']"
    cart_price_xpath = "//span[@class='product-unit-price']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_search_term(self, term):
        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.search_input_xpath)))
        search_input.clear()
        search_input.send_keys(term)

    def click_search_button(self):
        search_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_button_xpath)))
        search_button.click()

    def click_product_from_results(self):
        product_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.product_link_xpath)))
        product_link.click()

    def click_add_to_cart(self):
        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_xpath)))
        add_button.click()

    def get_cart_quantity(self):
        cart_qty = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.cart_quantity_xpath)))
        return cart_qty.text

    def click_login_link(self):
        login_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_link_xpath)))
        login_link.click()

    def enter_email(self, email):
        email_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.email_input_xpath)))
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.password_input_xpath)))
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button_xpath)))
        login_button.click()

    def verify_login_success(self):
        welcome = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.welcome_message_xpath)))
        return welcome.is_displayed()

    def click_shopping_cart(self):
        cart_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.shopping_cart_link_xpath)))
        cart_link.click()

    def verify_product_in_cart(self):
        product = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.cart_product_name_xpath)))
        return product.text == "Apple MacBook Pro"

    def get_cart_quantity_value(self):
        qty_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.cart_quantity_input_xpath)))
        return qty_input.get_attribute("value")

    def get_cart_price(self):
        price = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.cart_price_xpath)))
        return price.text