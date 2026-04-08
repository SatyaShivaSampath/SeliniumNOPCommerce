import pytest
from pages.pages5.change_password_page import ChangePasswordPage
 
 
class TestChangePassword:
 
    @pytest.mark.change_password
    def test_change_password_positive(self, driver):
 
        page = ChangePasswordPage(driver)
 
        page.open_homepage()
        assert "nopCommerce demo store" in driver.title
 
        page.click_login()
        page.login("randy@gmail.com", "viper12")
 
        page.go_to_my_account()
        page.open_change_password()
 
        page.change_password("viper12", "viper11")
 
        assert page.verify_password_changed()
