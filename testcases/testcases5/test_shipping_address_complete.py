import pytest
from pages.pages5.checkout_page import CheckoutPage


class TestShippingAddressComplete:

    @pytest.mark.checkout
    def test_shipping_address_verification(self, driver):
        """
        Test Case 26: Shipping Address Verification During Checkout
        
        Flow:
        1. User login
        2. Check cart - add product if empty, else proceed
        3. Go to checkout - billing address appears
        4. Uncheck "Ship to same address" checkbox
        5. Click continue - shipping address appears
        6. Verify shipping address matches My Account address
        7. If user has no address - create one first
        8. Handle all dropdowns properly
        """
        
        page = CheckoutPage(driver)
        
        # Step 1: Login
        print("[STEP 1] Opening homepage and logging in...")
        page.open_homepage()
        assert "nopCommerce demo store" in driver.title
        page.click_login()
        page.login("punk@gmail.com", "breaking")
        print("[PASS] User logged in successfully")
        
        # Step 2: Ensure the user has an account address
        print("\n[STEP 2] Ensuring user has a saved address in My Account...")
        account_address = page.ensure_account_address_exists()
        assert account_address, "Failed to ensure account has a saved address"
        print("[PASS] Account address exists")
        
        # Step 3: Check cart and add product if needed
        print("\n[STEP 3] Checking cart...")
        page.check_and_add_product_to_cart()
        print("[PASS] Cart verified and product added if needed")
        
        # Step 4: Go to checkout
        print("\n[STEP 4] Proceeding to checkout...")
        page.go_to_checkout_page()
        print("[PASS] On checkout page with billing address")
        
        # Step 5: Check billing address and uncheck "same address"
        print("\n[STEP 5] Checking billing address and unchecking 'Ship to same address'...")
        page.uncheck_ship_to_same_address()
        print("[PASS] Unchecked 'Ship to same address' checkbox")
        
        # Step 6: Click continue to proceed to shipping section
        print("\n[STEP 6] Clicking continue to proceed to shipping section...")
        page.click_billing_continue()
        print("[PASS] Proceeded to shipping section")
        
        # Step 7: Verify shipping address matches account address
        print("\n[STEP 7] Verifying shipping address matches account address...")
        is_match = page.verify_shipping_address_matches_account(account_address)
        assert is_match, "Shipping address does not match account address"
        print("[PASS] Shipping address matches account address!")
        
        print("\n[PASS] Test completed successfully!")
