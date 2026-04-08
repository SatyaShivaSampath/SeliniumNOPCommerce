from pages.pages2.my_account_page_verify import login_page_and_my_acc_verify
from pages.pages2.product_review_page import ProductReviewPage
import pytest,time

@pytest.mark.regression
def test_verify_product_review(driver):
    login_page = login_page_and_my_acc_verify(driver)
    assert login_page.verify_home_page() is True

    login_page.click_login_button()
    assert login_page.verify_the_login_page() is True

    login_page.enter_email("abcde.fghi@gmail.com")
    login_page.enter_password("AbcdeFghi_1234")
    login_page.click_login_button_to_enter()

    review_page = ProductReviewPage(driver)
    review_page.click_first_product()
    review_page.click_add_your_review()

    review_page.enter_review_title("Excellent product")
    review_page.enter_review_text("This product exceeded my expectations and works perfectly.")
    review_page.select_rating(3)
    review_page.click_submit_review()

    assert review_page.verify_success_message() is True
    review_page.close_notification()
    login_page.click_my_account_button()
    review_page.click_my_product_reviews()
    assert review_page.verify_my_product_reviews_page() is True
    assert review_page.verify_review_added("Excellent product") is True
