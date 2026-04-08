from selenium.webdriver.common.by import By

class ContactPage:
    contact_us_page = (By.XPATH,"//a[contains(text(),'Contact us')]")
    name_input = (By.ID, "FullName")
    email_input = (By.ID, "Email")
    enquiry_input = (By.ID, "Enquiry")
    submit_button = (By.NAME, "send-email")
    success_message = (By.XPATH, "//div[contains(text(), 'successfully sent')]")
    
    def __init__(self, driver):
        self.driver = driver    

    def submit_enquiry(self, name, email, enquiry):
        self.driver.find_element(*self.contact_us_page).click()  
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.enquiry_input).send_keys(enquiry)
        self.driver.find_element(*self.submit_button).click()
    
    def get_success_message(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(), 'successfully sent')]").text



