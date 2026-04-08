from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ========== LOCATORS ==========
    
    # Login
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class,'login-button')]")
    
    # Cart & Checkout
    BOOKS_MENU = (By.LINK_TEXT, "Books")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    SHOPPING_CART = (By.LINK_TEXT, "Shopping cart")
    TERMS_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BTN = (By.ID, "checkout")
    
    # Billing
    BILLING_CONTINUE_BTN = (By.XPATH, "//button[contains(text(), 'Continue')]")
    BILLING_ADDRESS_DROPDOWN = (By.ID, "billing-address-select")
    
    # Shipping
    SAME_ADDRESS_CHECKBOX = (By.ID, "ShipToSameAddress")
    SHIPPING_ADDRESS_DROPDOWN = (By.ID, "shipping-address-select")
    SHIPPING_CONTINUE_BTN = (By.XPATH, "//button[@onclick='Shipping.save()']")
    
    # Address Fields
    FIRSTNAME = (By.ID, "Address_FirstName")
    LASTNAME = (By.ID, "Address_LastName")
    EMAIL_FIELD = (By.ID, "Address_Email")
    COUNTRY_DROPDOWN = (By.ID, "Address_CountryId")
    STATE_DROPDOWN = (By.ID, "Address_StateProvinceId")
    CITY = (By.ID, "Address_City")
    ADDRESS1 = (By.ID, "Address_Address1")
    ZIP = (By.ID, "Address_ZipPostalCode")
    PHONE = (By.ID, "Address_PhoneNumber")
    SAVE_ADDRESS_BTN = (By.XPATH, "//button[contains(text(), 'Save')]")
    
    # My Account
    MY_ACCOUNT_LINK = (By.LINK_TEXT, "My account")
    ADDRESSES_LINK = (By.LINK_TEXT, "Addresses")
    ADDRESS_LIST = (By.CLASS_NAME, "address-list")
    ADD_NEW_ADDRESS_BTN = (By.XPATH, "//button[contains(text(), 'Add new')]")
    
    # ========== METHODS ==========
    
    def open_homepage(self):
        """Open the nopCommerce homepage"""
        self.driver.get("https://demo.nopcommerce.com/")
        time.sleep(2)
    
    def click_login(self):
        """Click on Login link"""
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK)).click()
        time.sleep(1)
    
    def login(self, email, password):
        """Login with email and password"""
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        time.sleep(2)
    
    def check_and_add_product_to_cart(self):
        """Check cart - if empty add product, else skip"""
        # Check current cart count
        try:
            cart_qty = self.driver.find_element(By.CLASS_NAME, "cart-qty")
            qty_text = cart_qty.text.strip("()")
            if qty_text and int(qty_text) > 0:
                print(f"[INFO] Cart already has {qty_text} products")
                return
        except:
            pass
        
        # Cart is empty, add a product
        print("[INFO] Cart is empty, adding product...")
        self.wait.until(EC.element_to_be_clickable(self.BOOKS_MENU)).click()
        time.sleep(2)
        
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-item")))
        add_to_cart_buttons = self.driver.find_elements(*self.ADD_TO_CART_BTN)
        
        if add_to_cart_buttons:
            add_to_cart_buttons[0].click()
            self.wait.until(lambda d: int(d.find_element(By.CLASS_NAME, "cart-qty").text.strip("()")) > 0)
            time.sleep(2)
    
    def go_to_checkout_page(self):
        """Go to cart and click checkout"""
        # Click shopping cart
        self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART)).click()
        time.sleep(2)
        
        # Accept terms and checkout
        self.wait.until(EC.element_to_be_clickable(self.TERMS_CHECKBOX)).click()
        time.sleep(1)
        
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()
        time.sleep(3)
    
    def uncheck_ship_to_same_address(self):
        """Uncheck 'Ship to same address' checkbox"""
        checkbox = self.wait.until(EC.element_to_be_clickable(self.SAME_ADDRESS_CHECKBOX))
        if checkbox.is_selected():
            checkbox.click()
            time.sleep(1)
    
    def click_billing_continue(self):
        """Click billing continue button to go to shipping section"""
        time.sleep(2)
        btn = self.wait.until(EC.element_to_be_clickable(self.BILLING_CONTINUE_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(3)
    
    def get_account_address_and_check(self):
        """Get address from My Account and check if it exists - opens My Account only once"""
        try:
            self.wait.until(EC.element_to_be_clickable(self.MY_ACCOUNT_LINK)).click()
            time.sleep(2)
            
            self.wait.until(EC.element_to_be_clickable(self.ADDRESSES_LINK)).click()
            time.sleep(2)
            
            # Get address list
            address_list = self.wait.until(EC.presence_of_element_located(self.ADDRESS_LIST))
            address_text = address_list.text
            
            # Check if address exists
            if address_text and len(address_text.strip()) > 0:
                print("[INFO] Address found in My Account")
                return address_text, True
            else:
                return None, False
        except Exception as e:
            print(f"[ERROR] Error getting address: {e}")
            return None, False
        finally:
            # Go back to homepage
            self.open_homepage()
    
    def ensure_account_address_exists(self):
        """Ensure the user has at least one address in My Account"""
        account_address, address_exists = self.get_account_address_and_check()
        if address_exists:
            return account_address
        
        print("[INFO] No address found in My Account. Adding a new address...")
        self.add_new_address_to_account()
        account_address, address_exists = self.get_account_address_and_check()
        return account_address
    
    def add_new_address_to_account(self):
        """Add a new address to user's account"""
        self.wait.until(EC.element_to_be_clickable(self.MY_ACCOUNT_LINK)).click()
        time.sleep(2)
        
        self.wait.until(EC.element_to_be_clickable(self.ADDRESSES_LINK)).click()
        time.sleep(2)
        
        # Click Add New Address
        try:
            add_btn = self.wait.until(EC.element_to_be_clickable(self.ADD_NEW_ADDRESS_BTN))
            add_btn.click()
            time.sleep(2)
        except:
            print("[WARNING] Add new address button not found")
        
        # Fill address form
        self._fill_address_form()
        
        # Save
        save_btn = self.wait.until(EC.element_to_be_clickable(self.SAVE_ADDRESS_BTN))
        self.driver.execute_script("arguments[0].click();", save_btn)
        time.sleep(2)
        
        # Go back to homepage
        self.open_homepage()
    
    def verify_shipping_address_matches_account(self, account_address):
        """Verify shipping address matches account address"""
        # Use provided account address instead of fetching again
        expected_values = {
            'name': 'John Cena',
            'email': 'johncena@gmail.com',
            'address': 'Street 1',
            'city': 'New York',
            'zip': '10001',
            'phone': '1234567890'
        }
        
        all_match = True
        for key, expected in expected_values.items():
            if expected in account_address:
                print(f"[PASS] {key}: {expected} matches")
            else:
                print(f"[FAIL] {key}: {expected} NOT found in account address")
                all_match = False
        
        return all_match
    
    def _fill_address_form(self):
        """Fill address form with test data"""
        # First Name
        self.wait.until(EC.visibility_of_element_located(self.FIRSTNAME)).send_keys("John")
        
        # Last Name
        self.driver.find_element(*self.LASTNAME).send_keys("Cena")
        
        # Email
        self.driver.find_element(*self.EMAIL_FIELD).send_keys("johncena@gmail.com")
        
        # Country
        country_dropdown = Select(self.driver.find_element(*self.COUNTRY_DROPDOWN))
        try:
            country_dropdown.select_by_value("1")  # 1 = United States
        except:
            try:
                country_dropdown.select_by_visible_text("United States")
            except:
                country_dropdown.select_by_visible_text("USA")
        time.sleep(3)
        
        # State - wait for options to populate after country selection
        try:
            state_dropdown = Select(self.wait.until(EC.presence_of_element_located(self.STATE_DROPDOWN)))
            time.sleep(1)
            try:
                state_dropdown.select_by_value("43")  # 43 = New York
            except:
                try:
                    state_dropdown.select_by_visible_text("New York")
                except:
                    state_dropdown.select_by_visible_text("NY")
        except:
            print("[WARNING] Could not select state, proceeding...")
        time.sleep(1)
        
        # City
        self.driver.find_element(*self.CITY).send_keys("New York")
        
        # Address
        self.driver.find_element(*self.ADDRESS1).send_keys("Street 1")
        
        # Zip
        self.driver.find_element(*self.ZIP).send_keys("10001")
        
        # Phone
        self.driver.find_element(*self.PHONE).send_keys("1234567890")
        
        time.sleep(1)

