from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Page object model for the login page of the Saucedemo website.
    Encapsulates the interactions with the login page elements.
    """
    #Selectors of the login fields
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        """
        Navigates the browser to the Saucedemo login page.

        This method loads the login page URL in the current browser window.
        """
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        """
        Perform the login action by entering the provided username and password and submitting the form.

        This method combines the steps of entering the username, entering the password, and clicking the login button.

        :param username: The username for the login.
        :param password: The password for the login.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()