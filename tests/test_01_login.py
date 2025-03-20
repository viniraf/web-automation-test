import pytest
from pages.login_page import LoginPage

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """
        Runs once before all tests in this class.
        Initializes and opens the login page.
        """
        self.login_page = LoginPage(driver)
        self.login_page.open()
        
    def test_login_empty_fields(self):
        """Test login attempt with empty username and password."""
        self.login_page.click_login_button()

        error_message = self.login_page.get_error_message()

        assert error_message == "Epic sadface: Username is required", f"Unexpected error message: {error_message}"

    def test_login_empty_password(self):
        """Test login attempt with username but empty password."""
        self.login_page.enter_username("standard_user")
        self.login_page.click_login_button()

        error_message = self.login_page.get_error_message()

        assert error_message == "Epic sadface: Password is required", f"Unexpected error message: {error_message}"

    def test_login_invalid_credentials(self):
        """Test login attempt with invalid username and password."""
        self.login_page.enter_username("invalid_user")
        self.login_page.enter_password("wrong_password")
        self.login_page.click_login_button()

        error_message = self.login_page.get_error_message()

        assert error_message == "Epic sadface: Username and password do not match any user in this service", f"Unexpected error message: {error_message}"

    def test_login_locked_out_user(self):
        """Test login attempt with a locked-out user."""
        self.login_page.login("locked_out_user", "secret_sauce")

        error_message = self.login_page.get_error_message()

        assert error_message == "Epic sadface: Sorry, this user has been locked out.", f"Unexpected error message: {error_message}"

    def test_login_valid(self):
        """
        Test a successful login with valid credentials.
        Ensures that after login, the user is redirected to the inventory page.
        """
        self.login_page.login("standard_user", "secret_sauce")

        assert self.login_page.driver.current_url == "https://www.saucedemo.com/inventory.html"