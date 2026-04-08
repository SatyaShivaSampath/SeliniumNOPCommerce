import pytest
@pytest.fixture
def driver():
    from selenium import webdriver
    driver=webdriver.Chrome()

    yield driver
    driver.close()
