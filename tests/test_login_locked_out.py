import pytest
from pages.login_page import LoginPage

def test_login_locked_out(setup):
    driver = setup
    
    login_page = LoginPage(driver)
    login_page.open()

    username = "locked_out_user"
    password = "secret_sauce"

    login_page.login(username, password)

    error_message_expected = "Epic sadface: Sorry, this user has been locked out."
    error_message_result = login_page.get_error_message()
    
    assert error_message_result == error_message_expected