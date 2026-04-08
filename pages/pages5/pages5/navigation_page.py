from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
 
class NavigationPage:
 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
 
    def delay(self, sec=2):
        time.sleep(sec)
 
    # Locators
    COMPUTERS = (By.LINK_TEXT, "Computers")
    ELECTRONICS = (By.LINK_TEXT, "Electronics")
    APPAREL = (By.LINK_TEXT, "Apparel")
    DIGITAL_DOWNLOADS = (By.LINK_TEXT, "Digital downloads")
    BOOKS = (By.LINK_TEXT, "Books")
    JEWELRY = (By.LINK_TEXT, "Jewelry")
    GIFT_CARDS = (By.LINK_TEXT, "Gift Cards")
 
    PAGE_TITLE = (By.TAG_NAME, "h1")
 
    def open_homepage(self):
        self.driver.get("https://demo.nopcommerce.com/")
        self.delay(3)
 
    def navigate_and_verify(self, locator, expected_text):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        self.delay(2)
 
        title = self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE)).text
        assert expected_text in title
 
        self.driver.back()
        self.delay(2)
 
    def verify_navigation_links(self):
        self.navigate_and_verify(self.COMPUTERS, "Computers")
        self.navigate_and_verify(self.ELECTRONICS, "Electronics")
        self.navigate_and_verify(self.APPAREL, "Apparel")
        self.navigate_and_verify(self.DIGITAL_DOWNLOADS, "Digital downloads")
        self.navigate_and_verify(self.BOOKS, "Books")
        self.navigate_and_verify(self.JEWELRY, "Jewelry")
        self.navigate_and_verify(self.GIFT_CARDS, "Gift Cards")
 