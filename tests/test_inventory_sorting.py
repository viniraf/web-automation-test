import pytest

from pages.inventory_page import InventoryPage

@pytest.mark.usefixtures("login_valid")
class TestInventorySorting:
    """
    Test cases for sorting functionality in the inventory page.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """
        Runs before each test in this class.
        Ensures that it is the inventory page before sorting.
        """
        self.inventory_page = InventoryPage(driver)    

    def test_sort_by_name_ascending(self):
        """
        Validates sorting by name A-Z.
        """
        self.inventory_page.select_sort_option("Name (A to Z)")
        product_names = self.inventory_page.get_product_names()
        assert product_names == sorted(product_names), "Sorting A-Z failed!"

    def test_sort_by_name_descending(self):
        """
        Validates sorting by name Z-A.
        """
        self.inventory_page.select_sort_option("Name (Z to A)")
        product_names = self.inventory_page.get_product_names()
        assert product_names == sorted(product_names, reverse=True), "Sorting Z-A failed!"

    def test_sort_by_price_low_to_high(self):
        """
        Validates sorting by price Low to High.
        """
        self.inventory_page.select_sort_option("Price (low to high)")
        product_prices = self.inventory_page.get_product_prices()
        assert product_prices == sorted(product_prices), "Sorting Low to High failed!"

    def test_sort_by_price_high_to_low(self):
        """
        Validates sorting by price High to Low.
        """
        self.inventory_page.select_sort_option("Price (high to low)")
        product_prices = self.inventory_page.get_product_prices()
        assert product_prices == sorted(product_prices, reverse=True), "Sorting High to Low failed!"