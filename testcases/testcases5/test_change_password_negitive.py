import pytest
from pages.change_password_page import ChangePasswordPage
 
 
class TestChangePasswordNegative:
 
    @pytest.mark.change_password
    def test_change_password_negative(self, driver):
        page = ChangePasswordPage(driver)
 
        page.open_homepage()
        assert "nopCommerce demo store" in driver.title
 
        page.click_login()
        page.login("scsa@gmail.com", "austin316")
 
        page.go_to_my_account()
        page.open_change_password()
 
        # Wrong old password
        page.change_password("Johncena@12", "Chandu@13")
 
        assert page.verify_old_password_error()
 