from pages.pages4.home_page import HomePage
from pages.pages4.category_page import CategoryPage
from pages.pages4.product_detail_page import ProductDetailPage

def test_verify_product_detail(setup):
    driver = setup
    driver.get("https://demo.nopcommerce.com/")

    home = HomePage(driver)
    assert home.is_home_page_visible()

    home.click_computers_category()
    category = CategoryPage(driver)
    category.click_notebooks()
    assert category.is_notebooks_page_visible()
    assert len(category.get_products_list()) > 0

    category.click_product("Apple MacBook Pro")

    product_page = ProductDetailPage(driver)
    assert product_page.get_product_name() == "Apple MacBook Pro"
    assert product_page.is_short_description_visible()
    assert product_page.get_product_price() == "$1,800.00"
    assert product_page.is_add_to_cart_visible()
    assert product_page.are_tabs_visible()