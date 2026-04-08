from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class CurrencyPage:
    
    home_page_title = "nopCommerce demo store"
    currency_dropdown = (By.ID, "customerCurrency")
    currency_usd = (By.XPATH, "//option[text()='US Dollar']")
    currency_euro = (By.XPATH, "//option[text()='Euro']")
    price_label = (By.CLASS_NAME, "prices")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def change_currency_to_euro(self):
        self.driver.find_element(*self.currency_dropdown).click()
        time.sleep(3)
        self.driver.find_element(*self.currency_euro).click()

    def change_currency_to_usd(self):
        self.driver.find_element(*self.currency_dropdown).click()
        time.sleep(3)
        self.driver.find_element(*self.currency_usd).click()
    
    def get_price_text(self):
        return self.driver.find_element(*self.price_label).text
        


