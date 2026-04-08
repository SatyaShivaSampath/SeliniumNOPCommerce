from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckoutPage:
    shopping_cart_link = (By.CLASS_NAME, "ico-cart")
    terms_checkbox = (By.ID, "termsofservice")
    checkout_button = (By.ID, "checkout")
    
    billing_address_dropdown = (By.ID, "billing-address-select")
    continue_button = (By.NAME, "save")
    
    fname_loc = (By.ID, "BillingNewAddress_FirstName")
    lname_loc = (By.ID, "BillingNewAddress_LastName")
    email_loc = (By.ID, "BillingNewAddress_Email")
    company_loc = (By.ID, "BillingNewAddress_Company")
    country_loc = (By.ID, "BillingNewAddress_CountryId")
    state_loc = (By.ID, "BillingNewAddress_StateProvinceId")
    city_loc = (By.ID, "BillingNewAddress_City")
    address1_loc = (By.ID, "BillingNewAddress_Address1")
    zip_code_loc = (By.ID, "BillingNewAddress_ZipPostalCode")
    phone_number_loc = (By.ID, "BillingNewAddress_PhoneNumber")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def go_to_checkout(self):
        self.driver.find_element(*self.shopping_cart_link).click()
        self.driver.find_element(*self.terms_checkbox).click()
        self.driver.find_element(*self.checkout_button).click()
    
    def is_address_present(self, expected_text):
        # dropdown = Select(self.driver.find_element(*self.billing_address_dropdown))
        # options = [opt.text for opt in dropdown.options]
        # return any(expected_text in opt for opt in options)
        elements = self.driver.find_elements(*self.billing_address_dropdown)
        if not elements:
            return False
        dropdown = Select(elements[0])
        options = [opt.text for opt in dropdown.options]
        return any(expected_text in opt for opt in options)

    def add_new_billing_address(self, fname, lname, email, company, country, state, city, address1, zip_code, phone):
        # If dropdown exists, select "New Address"
        elements = self.driver.find_elements(*self.billing_address_dropdown)
        if elements:
            dropdown = Select(elements[0])
            # Wait until "New Address" option is visible
            new_address_option = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//select[@id='billing-address-select']/option[text()='New Address']"))
            )
            new_address_option.click()

        # First name
        fname_el = self.wait.until(EC.visibility_of_element_located(self.fname_loc))
        fname_el.clear()
        fname_el.send_keys(fname)

        # Last name
        lname_el = self.wait.until(EC.visibility_of_element_located(self.lname_loc))
        lname_el.clear()
        lname_el.send_keys(lname)

        # Email
        email_el = self.wait.until(EC.visibility_of_element_located(self.email_loc))
        email_el.clear()
        email_el.send_keys(email)

        # Company
        company_el = self.wait.until(EC.visibility_of_element_located(self.company_loc))
        company_el.clear()
        company_el.send_keys(company)
        
        Select(self.driver.find_element(*self.country_loc)).select_by_visible_text(country)
        time.sleep(4)
        # self.wait.until(EC.element_to_be_clickable(self.state_loc))
        re=Select(self.driver.find_element(*self.state_loc))
        re.select_by_visible_text(state)

        self.wait.until(EC.visibility_of_element_located(self.city_loc)).send_keys(city)
        self.wait.until(EC.visibility_of_element_located(self.address1_loc)).send_keys(address1)
        self.wait.until(EC.visibility_of_element_located(self.zip_code_loc)).send_keys(zip_code)
        self.wait.until(EC.visibility_of_element_located(self.phone_number_loc)).send_keys(phone)
        time.sleep(3)
        self.driver.find_element(*self.continue_button).click()


