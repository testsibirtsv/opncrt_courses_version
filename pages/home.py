"""
Home Page Object Model
"""
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import logging

from pages.base import BasePage
from locators.home import HomePageLocators
from pages.product import ProductPage


logging.basicConfig(level=logging.INFO,
                    filename="my_log.log",
                    filemode="w")


class HomePage(BasePage):
    """
    Home Page Object Model
    """

    url = "http://127.0.0.1/opencart.com/index.php?route=common/home"

    def logging(self):
        """
        TODO
        """
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/a').click()
        self.driver.find_element_by_xpath('//*[@id="top-links"]/ul/li[2]/ul/li[2]/a').click()
        return self

    def input_email(self):
        """
        TODO
        """
        self.driver.find_element_by_id('input-email').send_keys('Nick123@gmail.com')
        return self

    def input_password(self):
        """
        TODO
        """
        self.driver.find_element_by_id('input-password').send_keys('123123123')
        return self

    def login(self):
        """
        TODO
        """
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/form/input').click()
        return self

    def go_to_home_page(self: object) -> object:
        """
        Go to Opencart home page.
        """
        self.driver.get("http://127.0.0.1/opencart.com/index.php?route=common/home")
        return self

    def is_on_home_page(self: object) -> bool:
        """
        Check the stay on the Home Page.
        """
        if self.driver.current_url == HomePage.url:
            logging.info('You are on the Opencart home page!')
            return True
        return False

    def click_on_shoping_cart_tab(self):
        """
        TODO
        """
        cart_tab = self.driver.find_element(*HomePageLocators.SHOPPING_CART_TAB)
        cart_tab.click()
        return self

    def click_on_components_tab(self):
        """
        TODO
        """
        components_tab = self.driver.find_element(*HomePageLocators.COMPONENTS_TAB)
        components_tab.click()
        return self

    def click_on_monitors(self):
        """
        TODO
        """
        monitors = self.driver.find_element(*HomePageLocators.MONITORS)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(HomePageLocators.MONITORS))
        monitors.click()
        return self

    def click_on_phones_tab(self):
        """
        TODO
        """
        phones = self.driver.find_element(*HomePageLocators.PHONES)
        phones.click()
        return self

    def go_to_product_id_41(self):
        """
        TODO
        """
        self.driver.get('http://localhost/index.php?route=product/product&product_id=41')
        return ProductPage(self.driver)

    def go_to_product_id_40(self):
        """
        TODO
        """
        self.driver.get('http://127.0.0.1/index.php?route=product/product&product_id=40')
        return ProductPage(self.driver)

    def select_mac_product(self):
        """Make webdriver click Mac product."""
        desktops = self.driver.find_element(*HomePageLocators.DESKTOPS_TAB)
        desktops.click()
        imac = self.driver.find_element(*HomePageLocators.MAC_GROUP)
        imac.click()
        return self

    def click_on_desktops_tab(self):
        """
        Make webdriver click  Product.
        :return:
        """
        desktops_tab = self.driver.find_element(*HomePageLocators.DESKTOPS_TAB)
        desktops_tab.click()
        return self

    def select_pc_product(self):
        """
        Make webdriver click pc product.
        :return: self
        """
        self.click_on_desktops_tab()
        pc_category = self.driver.find_element(*HomePageLocators.PC)
        pc_category.click()
        return self

    def list_category_desktops(self):
        """
        Make webdriver click desktop and take list of dropdown-menu.
         :return: list with elements on desktop category
        """
        self.click_on_desktops_tab()
        list_desktops = self.driver.find_elements(*HomePageLocators.LIST_DESKTOPS_TAB)
        return list_desktops

    def show_all_desktops(self):
        """
        Make webdriver click show all product
         :return: self
        """
        self.click_on_desktops_tab()
        all_desktops = self.driver.find_element(*HomePageLocators.SHOW_ALL_DESKTOPS)
        all_desktops.click()
        return self
