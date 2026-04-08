from pages2.my_account_page_verify import login_page_and_my_acc_verify
import pytest
@pytest.mark.order(1)
@pytest.mark.regression
def test_home_page_visible(driver):
    page = login_page_and_my_acc_verify(driver)
    assert page.verify_home_page() is True

@pytest.mark.order(2)
@pytest.mark.regression
def test_login_flow(driver):
    page = login_page_and_my_acc_verify(driver)
    page.click_login_button()
    assert page.verify_the_login_page() is True
    page.enter_email("abcde.fghi@gmail.com")
    page.enter_password("AbcdeFghi_1234")
    page.click_login_button_to_enter()
    page.click_my_account_button()
    assert page.to_verify_my_account() is True