"""
TODO
"""
from selenium.webdriver.common.by import By

# pylint: disable=too-few-public-methods
class BasePageLocators:
    """
    TODO
    """
    GO_CART = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a/i')
    QTY_IN_CART_INDICATOR = (By.ID, 'cart-total')
    SHOPPING_CART_TAB = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')
    DESKTOPS_TAB = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/a')
    COMPONENTS_TAB = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[3]/a')
    MONITORS = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[3]/div/div/ul/li[2]/a')
    PHONES = (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[6]/a')