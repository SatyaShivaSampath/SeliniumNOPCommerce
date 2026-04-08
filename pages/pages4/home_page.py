from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    computers_menu = (By.LINK_TEXT, "Computers")
    search_box = (By.ID, "small-searchterms")
    search_button = (By.CSS_SELECTOR, "button.search-box-button")

    def is_home_page_visible(self):
        return "nopCommerce demo store" in self.driver.title

    def enter_search_text(self, text):
        self.driver.find_element(*self.search_box).send_keys(text)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()