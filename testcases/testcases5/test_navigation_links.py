import pytest
from pages.pages5.navigation_page import NavigationPage
 
 
class TestNavigationLinks:
 
    @pytest.mark.navigation
    def test_navigation_links(self, driver):
        page = NavigationPage(driver)
 
        # Step 1-2
        page.open_homepage()
 
        # Step 3
        assert "nopCommerce demo store" in driver.title
 
        # Step 4
        page.verify_navigation_links()
