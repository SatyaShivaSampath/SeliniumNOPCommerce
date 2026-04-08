import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC

class PageAddToCart:

    #     locators
    electronics_link_xpath = "//a[text()='Electronics']"
    cell_phones_link_xpath = "//h2[@class='title']//a[text()=' Cell phones ']"
    mobile_link_xpath="//h2[@class='product-title']//a[@href='/htc-one-mini-blue']"
    mobile_add_to_cart_button_xpath = '//button[@id="add-to-cart-button-19"]'
    green_message_xpath = "//p[text()='The product has been added to your ']"
    green_message_close_xpath = "//span[@class='close']"
    shopping_cart_xpath="//span[text()='Shopping cart']"
    shopping_cart_link_xpath = "//a[@href='/cart']"

    cart_quantity_xpath="//span[@class='cart-qty']"

    # testcase-9
    # Locate the "Featured products" section
    featured_section_xpath =  "//h2[text()='Featured products']"
    build_your_own_computer_link_xpath = "//div[@class='picture']/a[@href='/build-your-own-computer']"
    build_your_own_computer_add_to_cart_xpath = "//button[@id='add-to-cart-button-1']"
    error_msg_required_attribute_xpath = "//p[text()='Please select RAM']"
    close_error_message_xpath = "//span[@class='close']"
    processor_dropdown_id = "product_attribute_1"
    ram_dropdown_id = "product_attribute_2"
    hdd_400gb_id = "product_attribute_3_7"
    office_checkbox_id = "product_attribute_5_10"
    acrobat_checkbox_id = "product_attribute_5_11"
    shopping_cart_link_xpath = "//a[@href='/cart']"
    # cart_quantity_xpath = "//span[@class='cart-qty']"
    cart_sku_xpath = "//span[@class='sku-number']"
    cart_product_name_xpath = "//a[@class='product-name']"
    os_option_id = "product_attribute_4_9"  # Example: Vista Home



    qty_up_button_xpath = "//div[@class='quantity up']"


# testcase 10
#     Update Quantity in Shopping Cart
    cart_quantity_input_xpath = "//input[@class='qty-input']"
    cart_subtotal_xpath = "//span[@class='product-subtotal']"
    update_cart_button_xpath = "//button[@name='updatecart']"

# Testcase-12:

    mini_cart_product_name_xpath = "//div[@class='name']"
    mini_cart_product_price_xpath = "//div[@class='price']"
    go_to_cart_button_xpath = "//div[@class='buttons']/input[@value='Go to cart']"
    mini_cart_dropdown_xpath = "//div[@id='flyout-cart']"

    computers_link_xpath = "//ul[@class='top-menu']//a[contains(text(),'Computers')]"
    notebooks_link_xpath = "//ul[@class='top-menu']//a[contains(text(),'Notebooks')]"
    macbook_link_xpath = "//h2[@class='product-title']/a[contains(text(),'Apple MacBook Pro 13-inch')]"
    add_to_cart_button_xpath = "//button[@id='add-to-cart-button-4']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_electronics_link(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.electronics_link_xpath))).click()

    def click_cell_phones_link(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.cell_phones_link_xpath))
        )
        element.click()

    def click_mobile_link(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.mobile_link_xpath))
        )
        element.click()

    def add_mobile_to_cart(self):
        # self.driver.wait_for_element(By.ID, self.mobile_add_to_cart_button_Id).click()
        # element = self.wait.until(EC.element_to_be_clickable((By.ID, self.mobile_add_to_cart_button_Id)))
        # element.click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.mobile_add_to_cart_button_xpath).click()

    def verify_product_added_message(self):
        # Wait until the green success message is visible
        element = self.wait.until(
            EC.invisibility_of_element_located((By.XPATH, self.green_message_xpath)))
        return element

    def close_green_message(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.green_message_close_xpath))
        )
        element.click()

    def get_cart_quantity(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.cart_quantity_xpath))
        )
        return element.text


# testcase-9:

    def scroll_to_featured_products(self):
        section = self.driver.find_element(By.XPATH, self.featured_section_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", section)
        return section

    def open_build_your_own_computer(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.build_your_own_computer_link_xpath))
        ).click()

    def click_add_to_cart_without_attributes(self):
        button = self.driver.find_element(By.XPATH, self.build_your_own_computer_add_to_cart_xpath)
        button.click()
        time.sleep(3)


    def get_error_message(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.error_msg_required_attribute_xpath))
        )
        return element.text

    def close_error_message(self):
        try:
            self.driver.find_element(By.XPATH, self.close_error_message_xpath).click()
        except Exception:
            print("Error message auto-closed or close button not found")

    def select_processor(self, option_text="2.2 GHz Intel Pentium Dual-Core E2200"):
        Select(self.driver.find_element(By.ID, self.processor_dropdown_id)).select_by_visible_text(option_text)


    def select_ram(self, option_text="2 GB"):
        Select(self.driver.find_element(By.ID, self.ram_dropdown_id)).select_by_visible_text(option_text)

    def select_hdd_400gb(self):
        self.driver.find_element(By.ID, self.hdd_400gb_id).click()

    def update_software_options(self):
        office_checkbox = self.driver.find_element(By.ID, self.office_checkbox_id)
        if office_checkbox.is_selected():
            office_checkbox.click()
        acrobat_checkbox = self.driver.find_element(By.ID, self.acrobat_checkbox_id)
        if not acrobat_checkbox.is_selected():
            acrobat_checkbox.click()

    def click_add_to_cart_req_attributes(self):
        self.driver.find_element(By.XPATH, self.build_your_own_computer_add_to_cart_xpath).click()

    def open_cart(self):
        self.driver.find_element(By.XPATH, self.shopping_cart_link_xpath).click()

    def get_cart_quantity(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.cart_quantity_xpath))
        )
        return element.text  # e.g. "(1)"

    def get_cart_sku(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.cart_sku_xpath))
        )
        return element.text  # e.g. "COMP_CUST"

    def get_cart_product_name(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.cart_product_name_xpath))
        )
        return element.text  # e.g. "Build your own computer"



    # testcase-10:
    def update_cart_quantity(self, new_qty):
        # Find the quantity input fresh
        for i in range(new_qty):
            self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.qty_up_button_xpath))
            ).click()
            time.sleep(1)
        time.sleep(3)

    def get_cart_unit_price(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.cart_unit_price_xpath))
        )
        return float(element.text.replace("$", "").replace(",", ""))

    def get_cart_subtotal(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.cart_subtotal_xpath))
        )
        return float(element.text.replace("$", "").replace(",", ""))

# testcase-11


    remove_checkbox_xpath = "//button[@class='remove-btn']"

    update_cart_button_xpath = "//button[@name='updatecart']"
    empty_cart_message_xpath = "//div[@class='order-summary-content']"

    def remove_product_from_cart(self):
        # Tick the remove checkbox
        remove_checkbox = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.remove_checkbox_xpath))
        )
        remove_checkbox.click()



    def is_cart_empty(self):
        msg = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.empty_cart_message_xpath))
        )
        return "Your Shopping Cart is empty!" in msg.text



    def hover_over_cart(self):
        cart_link = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.shopping_cart_xpath))
        )
        ActionChains(self.driver).move_to_element(cart_link).perform()
        # Wait for mini-cart dropdown to appear
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.mini_cart_dropdown_xpath))
        )

    def is_mini_cart_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.mini_cart_dropdown_xpath))
        ).is_displayed()

    def get_mini_cart_product_details(self):
        name = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.mini_cart_product_name_xpath))
        ).text
        price = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.mini_cart_product_price_xpath))
        ).text
        return name, price

