import pytest
from pages3.currency_page import CurrencyPage

@pytest.mark.order(7)
@pytest.mark.smoke
@pytest.mark.positive
def test_currency_conversion(driver):
    driver.get("https://demo.nopcommerce.com/")
    currency_page = CurrencyPage(driver)
    
    assert CurrencyPage.home_page_title in driver.title
    
    currency_page.change_currency_to_euro()
    price_text = currency_page.get_price_text()
    assert "€" in price_text
    
    currency_page.change_currency_to_usd()
    price_text = currency_page.get_price_text()
    assert "$" in price_text
    













