from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ProductPage:
    product_link = (By.XPATH, "//*[@id='main']/div/section/div/div/section[2]/div/div[3]/article/div[2]/div[3]/div[2]/button[1]")
    home_link = (By.XPATH, "//*[@alt='nopCommerce demo store']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_first_product_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.home_link)).click()
        # Click product link
        self.wait.until(EC.element_to_be_clickable(self.product_link)).click()
