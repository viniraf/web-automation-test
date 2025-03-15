from pages.login_page import LoginPage

def test_login_valid(setup):
    driver = setup

    login_page = LoginPage(driver)
    login_page.open()

    valid_username = "standard_user"
    valid_password = "secret_sauce"

    login_page.login(valid_username, valid_password)

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"