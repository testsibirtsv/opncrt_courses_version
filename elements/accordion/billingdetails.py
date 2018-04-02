from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements.base import BasePageElement
from locators.checkout import CheckoutPageLocators


class BillingDetails(BasePageElement):

    def __init__(self, driver):
        super().__init__(driver)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CheckoutPageLocators.FIRST_NAME))

        self.firstname = self.driver.find_element(*CheckoutPageLocators.FIRST_NAME)
        self.lastname = self.driver.find_element(*CheckoutPageLocators.LAST_NAME)
        self.email = self.driver.find_element(*CheckoutPageLocators.EMAIL)
        self.telephone = self.driver.find_element(*CheckoutPageLocators.TELEPHONE)
