import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Safari()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()