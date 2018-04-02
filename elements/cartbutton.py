"""
Cart Button Page Element.
"""

from elements.base import BasePageElement
from locators.cart import CartButtonLocators


class CartButton(BasePageElement):
    """
    Cart Button page element.
    """

    def click_on_cart_button(self: object) -> object:
        """
        Click on Cart Button.
        """
        cart_button = self.driver.find_element(*CartButtonLocators.CART_BUTTON)
        cart_button.click()
        return self
