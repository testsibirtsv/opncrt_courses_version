"""
Cart Page Object Model
"""
import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from elements.button import Button
from locators.product import ProductPageLocators
from pages.base import BasePage
from pages.checkout import CheckoutPage
from locators.cart import CartPageLocators


logging.basicConfig(level=logging.INFO,
                    filename="my_log.log",
                    filemode="w")


class CartPage(BasePage):
    """
    Cart Page Object Model
    """

    url = "http://127.0.0.1/opencart.com/index.php?route=checkout/cart"

    def __init__(self, driver):
        """
        Add checkout button element to the page
        """
        super().__init__(driver)
        self.checkout_btn = Button(driver, CartPageLocators.BTN_CHECKOUT)

    def edit_good_qty(self):
        """Make webdriver change qty of product in Cart"""
        edit_good_qty = self.driver.find_element(*CartPageLocators.GOOD_QTY_FIELD)
        edit_good_qty.clear()
        edit_good_qty.send_keys('2')
        update_good_qty = self.driver.find_element(*CartPageLocators.UPDATE_GOOD_QTY_BUTTON)
        update_good_qty.click()
        return self

    def delete_good_from_cart(self):
        """Make webdriver delete product from Cart."""
        delete_good = self.driver.find_element(*CartPageLocators.DELETE_GOOD_BUTTON)
        delete_good.click()
        return self

    def go_to_checkout(self):
        """
        TODO
        """
        self.checkout_btn.click()
        return CheckoutPage(self.driver)

    def is_on_cart_page(self: object) -> bool:
        """
        Check the stay on the Cart Page.
        """
        if self.driver.current_url == CartPage.url:
            logging.info("You are on the Cart page!")
            return True
        return False

    def is_cart_empty(self: object) -> bool:
        """
        Check whether cart is empty.
        """
        empty_cart_text = self.driver.find_element(*CartPageLocators.EMPTY_CART_TEXT)
        if empty_cart_text:
            logging.info("Your cart is empty!")
            return True
        return False

    def click_on_continue_button(self: object) -> object:
        """
        Click on continue button on Cart Page.
        """
        continue_button = self.driver.find_element(*CartPageLocators.CONTINUE_BUTTON)
        continue_button.click()
        return self
        return self

    def is_product_added(self: object) -> bool:
        """
        Check whether product is added to cart.
        """
        product_name = self.driver.find_element(*CartPageLocators.IPHONE_PRODUCT_NAME)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located(CartPageLocators.IPHONE_PRODUCT_NAME))
        if product_name.text == "iPhone":
            logging.info("You added iPhone!")
            return True
        print('Cart is empty!')
        return False

    def add_to_cart_apple_cinema(self: object) -> object:
        """
        Add Apple Cinema to cart.
        """
        add_to_cart_button = self.driver.find_element(*ProductPageLocators.ADD_APPLE_CINEMA)
        add_to_cart_button.click()
        return self

    def add_iphone_to_cart(self: object) -> object:
        """
        Add iPhone to cart.
        """
        add_to_cart_button = self.driver.find_element(*ProductPageLocators.ADD_IPHONE)
        add_to_cart_button.click()
        return self

    def delete_from_cart(self: object) -> object:
        """
        Delete product from cart.
        """
        delete_button = self.driver.find_element(*CartPageLocators.DELETE_GOOD_BUTTON)
        delete_button.click()
        return self
