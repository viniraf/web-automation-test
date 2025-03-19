from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

class InventoryPage:
    """
    Page Object Model for the inventory page of the Saucedemo website.
    Encapsulates interactions with sorting and product list.
    """

    # Element selectors
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    product_names = (By.CLASS_NAME, "inventory_item_name")
    product_prices = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_sort_option(self, option_text: str):
        """
        Selects a sorting option from the dropdown.

        :param option_text: Sorting option to select (e.g., 'Name (A to Z)', 'Price (low to high)')
        """
        sort_element = self.driver.find_element(*self.sort_dropdown)
        select = Select(sort_element)
        select.select_by_visible_text(option_text)

    def get_product_names(self):
        """
        Retrieves a list of product names currently displayed on the page.

        :return: List of product names (str)
        """
        elements = self.driver.find_elements(*self.product_names)
        return [element.text for element in elements]
    
    def get_product_prices(self):
        """
        Retrieves a list of product prices currently displayed on the page.

        :return: List of product prices (float)
        """
        elements = self.driver.find_elements(*self.product_prices)
        return [float(element.text.replace("$", "")) for element in elements]