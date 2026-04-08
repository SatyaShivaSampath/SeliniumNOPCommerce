# 13,14,,19,20
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class place_order_as_a_guest_user:
    #locators
    to_verify_the_visible_of_home_page_xapth="//img[@alt='nopCommerce demo store']"
    to_add_product_to_cart_by_clicking_add_to_button_for_navigation_text="//body/div[@class='master-wrapper-page']/main[@id='main']/div[@class='master-column-wrapper']/section[@class='center-1']/div[@class='page home-page']/div[@class='page-body']/section[@class='product-grid home-page-product-grid']/div[@class='item-grid']/div[2]/article[1]/div[2]/div[3]/div[2]/button[1]"
    to_add_the_product_to_cart_id="add-to-cart-button-4"
    to_click_shopping_cart_xpath="//a[@class='ico-cart']"
    to_check_the_agree_check_box_id="termsofservice"
    to_click_the_check_out_button_id="checkout"
    to_click_the_checkout_as_a_guest_button_xpath="//*[@class='button-1 checkout-as-guest-button']"
    
    fname_loc = "BillingNewAddress_FirstName"
    lname_loc = (By.ID, "BillingNewAddress_LastName")
    email_loc = (By.ID, "BillingNewAddress_Email")
    company_loc = (By.ID, "BillingNewAddress_Company")
    country_loc = (By.ID, "BillingNewAddress_CountryId")
    state_loc = (By.ID, "BillingNewAddress_StateProvinceId")
    city_loc = (By.ID, "BillingNewAddress_City")
    address1_loc = (By.ID, "BillingNewAddress_Address1")
    zip_code_loc = (By.ID, "BillingNewAddress_ZipPostalCode")
    phone_number_loc = (By.ID, "BillingNewAddress_PhoneNumber")
    click_continue_xpath="//*[@id='billing-buttons-container']/button[2]"
    shipping_method_by_id="shippingoption_0"
    click_continue_payment_method_xpath="//*[@id=billing-buttons-container']/button[2]"
    click_continue_payment_information_xapth="//*[@id='shipping-method-buttons-container']/button"
    click_continue_for_confirm_order_xpath="//*[@id='payment-method-buttons-container']/button"
    to_confirm_order_xpath="//*[@id='payment-info-buttons-container']/button"
    to_confirm_order_last_step_xpath="//*[@id='confirm-order-buttons-container']/button"
    to_verify_for_place_order="//*[text()='Your order has been successfully processed!']"
    to_verify_no_of_order_xpath="//*[@class='order-number']/strong"
    


    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)
    # methods
    def verify_home_page(self):
        return self.driver.find_element(By.XPATH, self.to_verify_the_visible_of_home_page_xapth).is_displayed()
    

    def add_product_to_cart_for_navigate(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.to_add_product_to_cart_by_clicking_add_to_button_for_navigation_text))
        ).click()
        
    def add_product_to_cart(self):
        self.driver.find_element(By.ID,self.to_add_the_product_to_cart_id).click()

    def click_shopping_cart(self):
        self.driver.find_element(By.XPATH, self.to_click_shopping_cart_xpath).click()

    def agree_terms(self):
        self.driver.find_element(By.ID, self.to_check_the_agree_check_box_id).click()

    def click_checkout(self):
        self.driver.find_element(By.ID, self.to_click_the_check_out_button_id).click()

    def click_check_out_as_guest_button(self):
        self.driver.find_element(By.XPATH,self.to_click_the_checkout_as_a_guest_button_xpath).click()

    def add_address(self, fname, lname, email, company, country, state, city, address1, zip_code, phone):
        
        first_name_field = self.wait.until(EC.visibility_of_element_located((By.ID,self.fname_loc)))
        first_name_field.clear()
        first_name_field.send_keys(fname)
        la=self.driver.find_element(*self.lname_loc)
        la.clear()
        la.send_keys(lname)
        res=self.driver.find_element(*self.email_loc)
        res.clear()
        res.send_keys(email)
        self.driver.find_element(*self.company_loc).send_keys(company)
    
        Select(self.driver.find_element(*self.country_loc)).select_by_visible_text(country)
        time.sleep(4)
        re=Select(self.driver.find_element(*self.state_loc))
        re.select_by_visible_text(state)
    
        self.driver.find_element(*self.city_loc).send_keys(city)
        self.driver.find_element(*self.address1_loc).send_keys(address1)
        self.driver.find_element(*self.zip_code_loc).send_keys(zip_code)
        self.driver.find_element(*self.phone_number_loc).send_keys(phone)

    def click_continue_billing(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.click_continue_xpath))).click()

    def click_continue_shipping_method(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.click_continue_payment_information_xapth))).click()

    def click_continue_payment_method(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.click_continue_for_confirm_order_xpath))).click()

    def click_continue_payment_info(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.to_confirm_order_xpath))).click()

    def click_confirm_order(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.to_confirm_order_last_step_xpath))).click()

    def to_confirm_order(self):
        re=self.driver.find_element(By.XPATH,self.to_verify_for_place_order).text
        return "Your order has been successfully processed!" in re

    def to_verify_no_of_order(self):
        re=self.driver.find_element(By.XPATH,self.to_verify_no_of_order_xpath).text
        return re 



    



        
