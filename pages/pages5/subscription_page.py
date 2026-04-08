from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
 
class SubscriptionPage:
 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
 
    # Delay function
    def delay(self, sec=2):
        time.sleep(sec)
 
    # Locators
    NEWSLETTER_INPUT = (By.ID, "newsletter-email")
    SUBSCRIBE_BUTTON = (By.ID, "newsletter-subscribe-button")
    SUCCESS_MESSAGE = (By.ID, "newsletter-result-block")
 
    # Methods
    def open_homepage(self):
        self.driver.get("https://demo.nopcommerce.com/")
        self.delay(3)
 
    def scroll_to_subscription(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.delay(2)
 
    def subscribe_newsletter(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.NEWSLETTER_INPUT)
        ).send_keys(email)
        self.delay(1)
 
        self.driver.find_element(*self.SUBSCRIBE_BUTTON).click()
        self.delay(2)
 
    def verify_subscription_success(self):
        message = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text
 
        print("Subscription message:", message)
 
        if "Thank you" in message:
            return True
        if "already subscribed" in message:
            return True
 
        return False
 