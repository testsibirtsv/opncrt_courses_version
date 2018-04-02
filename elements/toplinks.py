"""
Top Links page element.
"""

from elements.base import BasePageElement
from locators.base import BasePageLocators


class TopLinks(BasePageElement):
    """
    Top Links page element.
    """

    def cart_click(self):
        """
        TODO
        """
        self.cart = self.driver.find_element(*BasePageLocators.GO_CART)
        self.cart.click()

    def click_on_shopping_cart_tab(self: object) -> object:
        """
        Click on shopping cart tab.
        """
        cart_tab = self.driver.find_element(*BasePageLocators.SHOPPING_CART_TAB)
        cart_tab.click()
        return self
