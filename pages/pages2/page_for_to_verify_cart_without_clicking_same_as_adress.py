
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class place_order_with_out_click_same_adrress:
    to_uncheck_same_as_for_shipping_address="ShipToSameAddress"
    to_click_the_select_bar_id="shipping-address-select"
    fname_loc = "ShippingNewAddress_FirstName"
    lname_loc = (By.ID, "ShippingNewAddress_LastName")
    email_loc = (By.ID, "ShippingNewAddress_Email")
    company_loc = (By.ID, "ShippingNewAddress_Company")
    country_loc = (By.ID, "ShippingNewAddress_CountryId")
    state_loc = (By.ID, "ShippingNewAddress_StateProvinceId")
    city_loc = (By.ID, "ShippingNewAddress_City")
    address1_loc = (By.ID, "ShippingNewAddress_Address1")
    zip_code_loc = (By.ID, "ShippingNewAddress_ZipPostalCode")
    phone_number_loc = (By.ID, "ShippingNewAddress_PhoneNumber")
    click_continue_after_entering = "//*[@id='shipping-buttons-container']/button"


    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)

    def uncheck_same_as_for_shipping_address(self):
        self.driver.find_element(By.ID,self.to_uncheck_same_as_for_shipping_address).click()

    def to_select_the_new_adress(self):
        re=Select(self.driver.find_element(By.ID,self.to_click_the_select_bar_id))    
        re.select_by_visible_text("New Address")


    def add_address_shipment(self, fname, lname, email, company, country, state, city, address1, zip_code, phone):  
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

    def to_click_continue_after_entering(self):
        self.driver.find_element(By.XPATH,self.click_continue_after_entering).click()