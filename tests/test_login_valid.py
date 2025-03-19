def test_login_valid(login_valid):
    """
    Test a successful login with valid credentials.
    Ensures that after login, the user is redirected to the inventory page.
    """
    assert login_valid.driver.current_url == "https://www.saucedemo.com/inventory.html"