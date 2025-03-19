import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.fixture(scope="class")
def driver():
    """
    Fixture to initialize and close the WebDriver instance.
    This ensures a fresh browser session for each test.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def login_valid(driver):
    """
    Fixture to perform a valid login before executing the test.
    Ensures the user is authenticated and redirected to the inventory page.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    return login_page

@pytest.fixture
def login_locked(driver):
    """
    Fixture to attempt login with a locked-out user.
    Ensures the error message appears as expected.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message-container.error")))
    return login_page