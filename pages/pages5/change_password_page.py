from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
 
class ChangePasswordPage:
 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
 
    # Delay function to slow down execution
    def delay(self, seconds=2):
        time.sleep(seconds)
 
    # Locators
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class,'login-button')]")
 
    MY_ACCOUNT = (By.LINK_TEXT, "My account")
    CHANGE_PASSWORD = (By.LINK_TEXT, "Change password")
 
    OLD_PASSWORD = (By.ID, "OldPassword")
    NEW_PASSWORD = (By.ID, "NewPassword")
    CONFIRM_PASSWORD = (By.ID, "ConfirmNewPassword")
    CHANGE_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Change password']")
 
    SUCCESS_MESSAGE = (By.CLASS_NAME, "bar-notification")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='message-error validation-summary-errors']")
 
    # Methods
    def open_homepage(self):
        self.driver.get("https://demo.nopcommerce.com/")
        self.delay(3)
 
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK)).click()
        self.delay(2)
 
    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
        self.delay(1)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.delay(1)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.delay(3)
 
    def go_to_my_account(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_ACCOUNT)).click()
        self.delay(2)
 
    def open_change_password(self):
        self.wait.until(EC.element_to_be_clickable(self.CHANGE_PASSWORD)).click()
        self.delay(2)
 
    def change_password(self, old_pass, new_pass):
        self.wait.until(EC.visibility_of_element_located(self.OLD_PASSWORD)).send_keys(old_pass)
        self.delay(1)
        self.driver.find_element(*self.NEW_PASSWORD).send_keys(new_pass)
        self.delay(1)
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys(new_pass)
        self.delay(1)
        self.driver.find_element(*self.CHANGE_PASSWORD_BUTTON).click()
        self.delay(3)
 
    def verify_password_changed(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        self.delay(2)
        return "Password was changed" in self.driver.page_source
 
    def verify_old_password_error(self):
        self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        self.delay(2)
        return "Old password doesn't match" in self.driver.page_source