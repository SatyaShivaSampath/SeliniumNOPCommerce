from pages.pages4.home_page import HomePage
from pages.pages4.search_results_page import SearchResultsPage

def test_product_search(setup):
    driver = setup
    driver.get("https://demo.nopcommerce.com/")

    home = HomePage(driver)
    assert home.is_home_page_visible()

    # Step 4: Enter search text
    home.enter_search_text("Apple MacBook Pro")
    home.click_search_button()

    # Step 6–7: Verify search results
    results_page = SearchResultsPage(driver)
    assert results_page.is_product_present("Apple MacBook Pro")
    assert results_page.are_only_relevant_products_listed("Apple MacBook Pro")