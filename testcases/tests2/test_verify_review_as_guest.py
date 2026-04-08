from pages.pages2.my_account_page_verify import login_page_and_my_acc_verify
from pages.pages2.product_review_page import ProductReviewPage
import pytest

@pytest.mark.regression
def test_verify_review_as_guest(driver):

    login_page = login_page_and_my_acc_verify(driver)

    # Verify home page
    assert login_page.verify_home_page() is True

    review_page = ProductReviewPage(driver)

    # 4. Navigate to any product details page
    review_page.click_first_product()

    # 5. Click on 'Add your review'
    review_page.verify_unregistered_user_message()

    # 6. Verify that the system redirects to login page
    assert login_page.login_page_verify_the_login_button() is True
