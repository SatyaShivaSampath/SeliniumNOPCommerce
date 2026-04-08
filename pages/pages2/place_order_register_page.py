# 13,14,15,19,20
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class place_order_register_user:
    to_verify_the_visible_of_home_page_xapth="//img[@alt='nopCommerce demo store']"
    to_add_product_to_cart_by_clicking_add_to_button_for_navigation_text="//body/div[@class='master-wrapper-page']/main[@id='main']/div[@class='master-column-wrapper']/section[@class='center-1']/div[@class='page home-page']/div[@class='page-body']/section[@class='product-grid home-page-product-grid']/div[@class='item-grid']/div[2]/article[1]/div[2]/div[3]/div[2]/button[1]"
    to_add_the_product_to_cart_id="add-to-cart-button-4"
    to_click_shopping_cart_xpath="//a[@class='ico-cart']"
    to_check_the_agree_check_box_id="termsofservice"
    to_click_the_check_out_button_id="checkout"
    to_click_the_register_button_xpath="//a[@href='/register?returnUrl=%2Fcart']"
    to_mark_radio_button_for_male_id="gender-male"
    user_first_name_txt_input_id="FirstName"
    user_last_name_txt_input_id="LastName"
    user_email_txt_input_id="Email"
    user_company_txt_input_id="Company"
    user_click_news_latter_id="NewsLetterSubscriptions_0__IsActive"
    user_password_txt_input_id="Password"
    user_confirm_password_txt_input_id="ConfirmPassword"
    to_click_the_register_button_for_register_id="register-button"
    to_verify_after_registration_xpath="//div[text()='Your registration completed']"
    check_continue_button="//*[@id='main']/div/section/div/div[2]/div[2]/a"
    to_click_i_agree_id="termsofservice"
    after_clicking_register_to_check_thecheckout_id="checkout"

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

    def click_register_button(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.to_click_the_register_button_xpath))
        ).click()
    def fill_registration_form(self, firstname, lastname, email, company, password):
        self.driver.find_element(By.ID, self.to_mark_radio_button_for_male_id).click()
        self.driver.find_element(By.ID, self.user_first_name_txt_input_id).send_keys(firstname)
        self.driver.find_element(By.ID, self.user_last_name_txt_input_id).send_keys(lastname)
        self.driver.find_element(By.ID, self.user_email_txt_input_id).send_keys(email)
        self.driver.find_element(By.ID, self.user_company_txt_input_id).send_keys(company)
        self.driver.find_element(By.ID, self.user_password_txt_input_id).send_keys(password)
        self.driver.find_element(By.ID, self.user_confirm_password_txt_input_id).send_keys(password)
        self.driver.find_element(By.ID, self.to_click_the_register_button_for_register_id).click()

    def verify_registration_success(self):
        return self.driver.find_element(By.XPATH, self.to_verify_after_registration_xpath).is_displayed()
    
    def after_check_continue_button(self):
        self.driver.find_element(By.XPATH,self.check_continue_button).click()

    def to_click_i_agree(self):
        self.driver.find_element(By.ID,self.to_click_i_agree_id).click()

    def after_clicking_register_to_check_thecheckout(self):
        self.driver.find_element(By.ID,self.after_clicking_register_to_check_thecheckout_id).click()

    


        
