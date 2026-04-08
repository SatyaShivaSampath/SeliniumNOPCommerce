from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    register_link = (By.CLASS_NAME, "ico-register")
    gender_male = (By.ID, "gender-male")
    first_name = (By.ID, "FirstName")
    last_name = (By.ID, "LastName")
    email = (By.ID, "Email")
    company = (By.ID, "Company")
    password = (By.ID, "Password")
    confirm_password = (By.NAME, "ConfirmPassword")
    register_button = (By.ID, "register-button")
    success_message = (By.XPATH, "//div[contains(text(),'Your registration completed')]")
    error_message = (By.XPATH, "//li[contains(text(), 'The specified email already exists')]")
    logout_link = (By.CLASS_NAME, "ico-logout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def register(self, fname, lname, email, company, pwd):
        # Ensure homepage is loaded
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header-links")))
        # Click Register
        self.wait.until(EC.element_to_be_clickable(self.register_link)).click()
        # Fill form
        self.driver.find_element(*self.gender_male).click()
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.company).send_keys(company)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.confirm_password).send_keys(pwd)
        self.driver.find_element(*self.register_button).click()

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.success_message)).text
    
    def get_error_messages(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_message)).text

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.logout_link)).click()
