import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("login_valid")
class TestCheckout:
    """
    Test cases for the checkout process.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Runs before each test to ensure an empty cart."""
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_page = CheckoutPage(driver)
        self.cart_page.open_cart()
        self.cart_page.clear_cart()
        self.cart_page.continue_to_shopping()

    def test_checkout_form_validations(self):
        """Tests validation messages when required fields are missing."""
        products = self.inventory_page.get_product_names()
        product_name = products[0]
        print(f"[STEP] Adding product to cart: {product_name}")
        self.inventory_page.add_to_cart_by_name(product_name)

        self.cart_page.open_cart()
        print("[STEP] Opened cart and proceeding to checkout")
        self.checkout_page.start_checkout()

        print("[STEP] Filling checkout form without first name...")
        self.checkout_page.fill_checkout_form()
        expected_error = "Error: First Name is required"
        actual_error = self.checkout_page.get_error_message()
        print(f"[ASSERT] Expected: '{expected_error}', Got: '{actual_error}'")
        assert actual_error == expected_error

        print("[STEP] Filling checkout form without last name...")
        self.checkout_page.fill_checkout_form(first_name="John")
        expected_error = "Error: Last Name is required"
        actual_error = self.checkout_page.get_error_message()
        print(f"[ASSERT] Expected: '{expected_error}', Got: '{actual_error}'")
        assert actual_error == expected_error

        print("[STEP] Filling checkout form without postal code...")
        self.checkout_page.fill_checkout_form(first_name="John", last_name="Doe")
        expected_error = "Error: Postal Code is required"
        actual_error = self.checkout_page.get_error_message()
        print(f"[ASSERT] Expected: '{expected_error}', Got: '{actual_error}'")
        assert actual_error == expected_error

    def test_checkout_single_item(self):
        """Tests the checkout process with a single item, validating details and completion."""
        product_name = self.inventory_page.get_product_names()[0]
        print(f"[STEP] Adding single item to cart: {product_name}")
        self.inventory_page.add_to_cart_by_name(product_name)
        
        self.cart_page.open_cart()
        print("[STEP] Opened cart and proceeding to checkout")
        self.checkout_page.start_checkout()

        print("[STEP] Filling checkout form...")
        self.checkout_page.fill_checkout_form("John", "Doe", "12345")
        
        checkout_items = self.checkout_page.get_checkout_item_details()
        print(f"[ASSERT] Checking if product is in checkout: {product_name} is in checkout!")
        assert any(product_name in item for item in checkout_items), "Product name not found in checkout"
        
        print("[STEP] Finishing checkout")
        self.checkout_page.finish_checkout()
        expected_message = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        actual_message = self.checkout_page.get_complete_message()
        print(f"[ASSERT] Expected: '{expected_message}', Got: '{actual_message}'")
        assert actual_message == expected_message

    def test_checkout_multiple_items(self):
        """Tests the checkout process with multiple items, validating details and completion."""
        product_names = self.inventory_page.get_product_names()[:3]
        print(f"[STEP] Adding multiple items to cart: {product_names}")
        for name in product_names:
            self.inventory_page.add_to_cart_by_name(name)
        
        self.cart_page.open_cart()
        print("[STEP] Opened cart and proceeding to checkout")
        self.checkout_page.start_checkout()

        print("[STEP] Filling checkout form...")
        self.checkout_page.fill_checkout_form("John", "Doe", "12345")
        
        checkout_items = self.checkout_page.get_checkout_item_details()
        for name in product_names:
            print(f"[ASSERT] Checking if product is in checkout: {name} is in checkout!")
            assert any(name in item for item in checkout_items), f"Expected {name} in checkout overview"
        
        print("[STEP] Finishing checkout")
        self.checkout_page.finish_checkout()
        expected_message = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        actual_message = self.checkout_page.get_complete_message()
        print(f"[ASSERT] Expected: '{expected_message}', Got: '{actual_message}'")
        assert actual_message == expected_message