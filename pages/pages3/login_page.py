import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    login_link = (By.XPATH, "//a[@href='/login?returnUrl=%2F']")
    email_input = (By.ID, "Email")
    password_input = (By.ID, "Password")
    login_button = (By.XPATH, "//button[text()='Log in']")
    logout_link = (By.XPATH, "//a[@class='ico-logout']")
    error_message = (By.XPATH, "//div[contains(text(),'unsuccessful')]")

    prod_comp_link = (By.XPATH,"//a[text()='Compare products list']")
    prod1 = (By.XPATH,"//a[text()='Apple MacBook Pro']")
    prod2 = (By.XPATH,"//a[text()='HTC smartphone']")
    add_to_comparison = (By.XPATH,"//div[@class='overview']//button[text()='Add to compare list']")
    clear_list_button = (By.CLASS_NAME,"clear-list")
    empty_message = (By.CLASS_NAME,"no-data")
    
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, email, password):
        self.driver.find_element(*self.login_link).click()
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
    
    def product_comparison(self):
        # Add first product
        self.driver.find_element(*self.prod1).click()
        time.sleep(5)
        self.driver.find_element(*self.add_to_comparison).click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)

        # Add second product
        self.driver.find_element(*self.prod2).click()
        time.sleep(3)
        self.driver.find_element(*self.add_to_comparison).click()
        time.sleep(3)

        # Go to comparison page
        self.driver.find_element(*self.prod_comp_link).click()
        time.sleep(5)
        
        page_source = self.driver.page_source
        assert "Apple MacBook Pro" in page_source
        assert "HTC smartphone" in page_source

        # Clear the list
        self.driver.find_element(*self.clear_list_button).click()
        time.sleep(3)

        # Verify empty message
        return self.driver.find_element(*self.empty_message).text

        
    
    def is_logged_in(self):
        return "Log out" in self.wait.until(EC.visibility_of_element_located(self.logout_link)).text
    
    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text
    
    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.logout_link)).click()
