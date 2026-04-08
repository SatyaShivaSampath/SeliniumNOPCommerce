import pytest
import random
from pages.pages5.subscription_page import SubscriptionPage
 
 
class TestSubscription:
 
    @pytest.mark.subscription
    def test_newsletter_subscription(self, driver):
        page = SubscriptionPage(driver)
 
        # Step 1-2
        page.open_homepage()
 
        # Step 3
        assert "nopCommerce demo store" in driver.title
 
        # Step 4
        page.scroll_to_subscription()
 
        # Random email every run
        email = f"test{random.randint(1000,9999)}@gmail.com"
        page.subscribe_newsletter(email)
 
        # Step 5
        assert page.verify_subscription_success()
 
