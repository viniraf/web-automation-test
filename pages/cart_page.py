from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    """
    Page Object Model for the Cart page.
    Provides methods to interact with cart elements.
    """

    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_items = (By.CLASS_NAME, "cart_item")
    remove_button = (By.CLASS_NAME, "cart_button")
    checkout_button = (By.ID, "checkout")
    continue_to_shopping_button = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        """Clicks the cart icon to open the cart page."""
        self.driver.find_element(*self.cart_icon).click()

    def get_cart_count(self):
        """Returns the number displayed on the cart icon (items count)."""
        try:
            return int(self.driver.find_element(*self.cart_icon).text)
        except:
            return 0  # If no number, cart is empty

    def get_cart_items(self):
        """Returns a list of all items in the cart."""
        return self.driver.find_elements(*self.cart_items)
    
    def get_cart_item_names(self):
        """
        Returns a list of item names present in the cart.
        """
        items = self.driver.find_elements(*self.cart_items)  # Obtém todos os itens do carrinho
        names = [item.find_element(By.CLASS_NAME, "inventory_item_name").text for item in items]
        return names

    def clear_cart(self):
        """
        Removes all items from the cart if any exist, ensuring minimal delay.

        - First, it sets `implicitly_wait(0)` to avoid unnecessary waiting.
        - Then, it checks if there are cart items.
          - If the cart is empty, it exits immediately.
          - Otherwise, it restores `implicitly_wait(10)` for normal operation.
        - If items exist, it attempts to remove them one by one.
        - A `WebDriverWait` of 1 second is used to confirm item presence before removal.
        """
        # Set an explicit wait time of 0 to avoid unnecessary delays while checking cart items
        self.driver.implicitly_wait(0)  
        cart_items = self.driver.find_elements(*self.cart_items)

        if not cart_items:
            print("No items in the cart. Skipping removal.")
            return  

        # Restore the default wait time to avoid affecting other operations
        self.driver.implicitly_wait(10)  

        # Wait briefly (1 second) to confirm item presence before proceeding
        try:
            WebDriverWait(self.driver, 1).until(EC.presence_of_element_located(self.cart_items))
        except:
            print("No items found after waiting briefly. Skipping removal.")
            return

        for item in cart_items:
            try:
                remove_button = item.find_element(By.CLASS_NAME, "cart_button")
                remove_button.click()
            except Exception as e:
                print(f"Error removing item: {e}")

    def continue_to_shopping(self):
        self.driver.find_element(*self.continue_to_shopping_button).click()
