from pages2.my_account_page_verify import login_page_and_my_acc_verify
from pages2.wishlist_page import WishlistPage
import pytest, time

@pytest.mark.regression
def test_verify_wishlist(driver):
    login_page = login_page_and_my_acc_verify(driver)
    assert login_page.verify_home_page() is True

    login_page.click_login_button()

    assert login_page.verify_the_login_page() is True

    login_page.enter_email("abcde.fghi@gmail.com")
    login_page.enter_password("AbcdeFghi_1234")

    login_page.click_login_button_to_enter()

    wishlist_page = WishlistPage(driver)
    wishlist_page.add_product_to_wishlist_for_navigate()
    time.sleep(2)
    wishlist_page.add_product_to_wishlist()
    
    wishlist_page.click_wishlist()


    wishlist_page.select_all_items_and_add_to_cart()

    wishlist_page.click_add_to_cart()
    time.sleep(2)

    assert wishlist_page.verify_shopping_cart_page() is True