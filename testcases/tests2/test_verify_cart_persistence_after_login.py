from pages2.my_account_page_verify import login_page_and_my_acc_verify
from pages2.search_and_cart_page import SearchAndCartPage
import pytest, time

@pytest.mark.regression
def test_verify_cart_persistence_after_login(driver):
    # 2. Navigate to url (handled by fixture)
    # 3. Verify home page
    login_page = login_page_and_my_acc_verify(driver)
    assert login_page.verify_home_page() is True

    cart_page = SearchAndCartPage(driver)

    # 4. Enter 'Apple MacBook Pro' in search and click Search
    cart_page.enter_search_term("Apple MacBook Pro")
    cart_page.click_search_button()

    # 5. Click on the product from search results
    cart_page.click_product_from_results()

    # 6. Click Add to cart
    time.sleep(2)  
    cart_page.click_add_to_cart()


    cart_page.click_login_link()

    # 9. Enter valid email and password
    cart_page.enter_email("abcde.fghi@gmail.com")
    cart_page.enter_password("AbcdeFghi_1234")

    # 10. Click Log in
    cart_page.click_login_button()

    # 11. Verify logged in
    assert cart_page.verify_login_success() is True

    # 12. Click Shopping cart
    cart_page.click_shopping_cart()

    # 13. Verify product still in cart
    assert cart_page.verify_product_in_cart() is True

    # 14. Verify quantity and price
    assert int(cart_page.get_cart_quantity_value()) >= 1
    # Price verification - assuming $1,800.00 for MacBook Pro
    assert "$1,800.00" in cart_page.get_cart_price()