from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    """
    Page Object Model for the Checkout process.
    Provides methods to interact with checkout elements.
    """

    checkout_button = (By.ID, "checkout")
    first_name_input = (By.ID, "first-name")
    last_name_input = (By.ID, "last-name")
    postal_code_input = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    error_message = (By.CSS_SELECTOR, ".error-message-container.error h3[data-test='error']")
    inventory_item_name = (By.CLASS_NAME, "inventory_item_name")
    inventory_item_desc = (By.CLASS_NAME, "inventory_item_desc")
    inventory_item_price = (By.CLASS_NAME, "inventory_item_price")
    finish_button = (By.ID, "finish")
    complete_text = (By.CLASS_NAME, "complete-text")

    def __init__(self, driver):
        self.driver = driver

    def start_checkout(self):
        """Clicks the checkout button to begin the process."""
        self.driver.find_element(*self.checkout_button).click()

    def fill_checkout_form(self, first_name="", last_name="", postal_code=""):
        """Fills in the checkout form with the provided details."""
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_error_message(self):
        """Returns the checkout error message if present."""
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return None

    def get_checkout_item_details(self):
        """Returns item details from the checkout overview page."""
        names = [el.text for el in self.driver.find_elements(*self.inventory_item_name)]
        descriptions = [el.text for el in self.driver.find_elements(*self.inventory_item_desc)]
        prices = [el.text for el in self.driver.find_elements(*self.inventory_item_price)]
        return list(zip(names, descriptions, prices))

    def finish_checkout(self):
        """Completes the checkout process."""
        self.driver.find_element(*self.finish_button).click()

    def get_complete_message(self):
        """Returns the order completion message."""
        return self.driver.find_element(*self.complete_text).text
