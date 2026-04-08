from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductReviewPage:
    first_product_link_xpath = "(//h2[@class='product-title']/a)[1]"
    add_review_link_xpath = "//a[normalize-space()='Add your review']"
    text_for_unregistered_user_xpath = "//div[@class='result review-already-added']"
    product_reviews_heading_xpath = "//h1[normalize-space()='Product reviews']"
    review_title_input_xpath = "//input[@id='AddProductReview_Title']"
    review_text_input_xpath = "//textarea[@id='AddProductReview_ReviewText']"
    rating_radio_xpath = "//input[@type='radio' and @value='{}']"
    submit_review_button_xpath = "//button[@name='add-review']"
    success_message_xpath = "//*[@id='bar-notification']/div/p"
    click_my_account_button_xpath = "//a[@class='ico-account']"
    to_close_notification_xpath = "//*[@id='bar-notification']//span[@class='close']"
    my_product_reviews_link_xpath = "//a[@href='/customer/productreviews']"
    my_product_reviews_heading_xpath = "//*[@class='page-title']/h1"
    review_title_text_xpath = "//div[contains(@class,'review-title') and normalize-space()='{}']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_first_product(self):
        product_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.first_product_link_xpath)))
        product_link.click()

    def click_add_your_review(self):
        add_review = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_review_link_xpath)))
        add_review.click()

    def verify_product_reviews_page(self):
        heading = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.product_reviews_heading_xpath)))
        return heading.is_displayed()

    def enter_review_title(self, title):
        title_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.review_title_input_xpath)))
        title_input.send_keys(title)

    def enter_review_text(self, text):
        text_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.review_text_input_xpath)))
        text_input.send_keys(text)

    def select_rating(self, stars):
        rating_locator = (By.XPATH, self.rating_radio_xpath.format(stars))
        rating_input = self.wait.until(EC.element_to_be_clickable(rating_locator))
        rating_input.click()

    def click_submit_review(self):
        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.submit_review_button_xpath)))
        submit_button.click()

    def verify_success_message(self):
        message = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.success_message_xpath)))
        return message.is_displayed()

    def click_my_account_button(self):
        account_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.click_my_account_button_xpath)))
        account_btn.click()

    def close_notification(self):
        close_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.to_close_notification_xpath)))
        close_btn.click()

    def click_my_product_reviews(self):
        account_reviews_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.my_product_reviews_link_xpath)))
        account_reviews_link.click()

    def verify_my_product_reviews_page(self):
        heading = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.my_product_reviews_heading_xpath)))
        return heading.is_displayed()

    def verify_review_added(self, title):
        review_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.review_title_text_xpath.format(title))))
        return review_title.is_displayed()
    

    def verify_unregistered_user_message(self):
        message = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.text_for_unregistered_user_xpath)))
        return message.is_displayed()
