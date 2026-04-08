
from selenium.webdriver.common.by import By
class login_page_and_my_acc_verify:
    to_verify_the_visible_of_home_page_xapth="//img[@alt='nopCommerce demo store']"
    to_click_login_button="//*[@href='/login?returnUrl=%2F']"
    to_verify_login_page_visible="//h2[normalize-space()='Returning Customer']"
    to_input_email="//*[@class='email']"
    login_button_visible_xpath="//*[@href='/login?returnUrl=%2Fbuild-your-own-computer']"
    to_input_password="Password"
    to_click_login_button_for_login="//*[@class='button-1 login-button']"
    to_click_my_account_button="//*[@href='/customer/info' and @class='ico-account']"
    to_verify_the_my_account_page="//h1[normalize-space()='My account - Customer info']"

    def __init__(self,driver):
        self.driver=driver

    def verify_home_page(self):
        return self.driver.find_element(By.XPATH, self.to_verify_the_visible_of_home_page_xapth).is_displayed()
    
    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.to_click_login_button).click()

    def verify_the_login_page(self):
        re=self.driver.find_element(By.XPATH,self.to_verify_login_page_visible).text
        return "Returning Customer" in re
    
    def enter_email(self,email):
        self.driver.find_element(By.XPATH,self.to_input_email).send_keys(email)

    def enter_password(self,pwd):
        self.driver.find_element(By.ID,self.to_input_password).send_keys(pwd)

    def click_login_button_to_enter(self):
        self.driver.find_element(By.XPATH,self.to_click_login_button_for_login).click()


    def click_my_account_button(self):
        self.driver.find_element(By.XPATH,self.to_click_my_account_button).click()


    def to_verify_my_account(self):
        re=self.driver.find_element(By.XPATH,self.to_verify_the_my_account_page).text
        return "My account - Customer info" in re
    
    def login_page_verify_the_login_button(self):
        return self.driver.find_element(By.XPATH,self.login_button_visible_xpath).is_displayed()

