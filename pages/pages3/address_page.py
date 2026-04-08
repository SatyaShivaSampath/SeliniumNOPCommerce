from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

class AddressPage:
    
    my_account_link = (By.CLASS_NAME, "ico-account")
    address_link = (By.LINK_TEXT, "Addresses")
    add_new_button = (By.XPATH, "//button[text()='Add new']")
    delete_button_loc = (By.XPATH,"//button[text()='Delete']")

    fname_loc = (By.ID, "Address_FirstName")
    lname_loc = (By.ID, "Address_LastName")
    email_loc = (By.ID, "Address_Email")
    company_loc = (By.ID, "Address_Company")
    country_loc = (By.ID, "Address_CountryId")
    state_loc = (By.ID, "Address_StateProvinceId")
    city_loc = (By.ID, "Address_City")
    address1_loc = (By.ID, "Address_Address1")
    zip_code_loc = (By.ID, "Address_ZipPostalCode")
    phone_number_loc = (By.ID, "Address_PhoneNumber")
    save_button_loc = (By.XPATH, "//button[text()='Save']")
    address_box = (By.CLASS_NAME, "address-list")
    
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def navigate_to_address(self):
        self.wait.until(EC.element_to_be_clickable(self.my_account_link)).click()
        self.wait.until(EC.element_to_be_clickable(self.address_link)).click()

    
    def add_new_address(self, fname, lname, email, company, country, state, city, address1, zip_code, phone):
        self.wait.until(EC.element_to_be_clickable(self.add_new_button)).click()
        
        first_name_field = self.wait.until(EC.visibility_of_element_located(self.fname_loc))
        
        first_name_field.send_keys(fname)
        self.driver.find_element(*self.lname_loc).send_keys(lname)
        self.driver.find_element(*self.email_loc).send_keys(email)
        self.driver.find_element(*self.company_loc).send_keys(company)
        
        Select(self.driver.find_element(*self.country_loc)).select_by_visible_text(country)
        time.sleep(4)
        # self.wait.until(EC.element_to_be_clickable(self.state_loc))
        re=Select(self.driver.find_element(*self.state_loc))
        re.select_by_visible_text(state)
        
        self.driver.find_element(*self.city_loc).send_keys(city)
        self.driver.find_element(*self.address1_loc).send_keys(address1)
        self.driver.find_element(*self.zip_code_loc).send_keys(zip_code)
        self.driver.find_element(*self.phone_number_loc).send_keys(phone)
        
        self.driver.find_element(*self.save_button_loc).click()

    def verify_address_added(self, expected_text):
        address_list = self.wait.until(EC.visibility_of_element_located(self.address_box)).text
        return expected_text in address_list
    
    def remove_address(self):
        time.sleep(3)
        self.driver.find_element(*self.delete_button_loc).click()
        time.sleep(3)
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
    
    def verify_address_removed(self,expected_text):
        address_list = self.driver.find_elements(*self.address_box)
        return expected_text not in address_list

