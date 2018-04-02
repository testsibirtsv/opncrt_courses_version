"""
In this module class BasePage constructor will take argument driver,
which has to be returned by DriverFactory().create_web_driver(driver_name)
method
"""

from selenium import webdriver

from elements.navbar import NavBar
from elements.toplinks import TopLinks


class BasePage:
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver=None, url='/'):
        self.url = url
        self.driver = driver if driver else webdriver.Chrome()
        self.top_links = TopLinks(self.driver)
        self.navbar = NavBar(self.driver)

    def title(self)-> str:
        """
        function to get a title
        :return: title of page
        """
        return self.driver.title

    def to_home(self):
        """
        TODO
        """

    def to_cart(self):
        """
        TODO
        """
