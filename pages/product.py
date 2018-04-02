"""
Object Model for Product Page
"""
from elements.button import Button
from pages.base import BasePage
from pages.cart import CartPage
from locators.product import ProductPageLocators


class ProductPage(BasePage):
    """
    Product page action methods come here
    """

    def __init__(self, driver):
        """
        Add cart button element to the page
        """
        super().__init__(driver)
        self.cart_btn = Button(driver, ProductPageLocators.BTN_CART)

    def add_to_cart(self):
        """
        Click on cart button
        """
        self.cart_btn.click()
        return self

    def go_to_cart(self):
        """
        Go to Cart Page
        """
        self.top_links.cart_click()
        return CartPage(self.driver)

    def add_to_cart_apple_cinema(self):
        """
        TODO
        """
        add_to_cart_button = self.driver.find_element(*ProductPageLocators.ADD_APPLE_CINEMA)
        add_to_cart_button.click()
        return self

    def add_mac_to_cart(self):
        """Make webdriver add Mac product to Cart."""
        get_to_imac = self.driver.find(*ProductPageLocators.GO_TO_IMAC)
        get_to_imac.click()
        add_mac_to_cart = self.driver.find_element(*ProductPageLocators.ADD_IMAC_TO_CART)
        add_mac_to_cart.click()
        return self
