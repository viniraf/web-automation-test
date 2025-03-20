import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("login_valid")
class TestCart:
    """
    Test cases for shopping cart functionality.
    Ensures items are added and displayed correctly.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """
        Runs before each test to ensure an empty cart.
        """
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.cart_page.open_cart()
        self.cart_page.clear_cart()
        self.cart_page.continue_to_shopping()
        
    def test_add_single_item_to_cart(self):
        """
        Tests adding a single item to the cart and verifying the cart count.
        """
        products = self.inventory_page.get_product_names()
        product_name = products[0]
        self.inventory_page.add_to_cart_by_name(product_name)

        assert self.cart_page.get_cart_count() == 1, "Cart count should be 1"
        
        self.cart_page.open_cart()
        cart_item_names = self.cart_page.get_cart_item_names()

        assert product_name in cart_item_names, f"Expected {product_name} in cart"

    def test_add_multiple_items_to_cart(self):
        """
        Tests adding multiple items to the cart and verifying the cart count.
        """
        product_names = self.inventory_page.get_product_names()[:3]

        for name in product_names:
            self.inventory_page.add_to_cart_by_name(name)

        assert self.cart_page.get_cart_count() == 3, "Cart count should be 3"
        
        self.cart_page.open_cart()
        cart_item_names = self.cart_page.get_cart_item_names()
        for name in product_names:
            assert name in cart_item_names, f"Expected {name} in cart"