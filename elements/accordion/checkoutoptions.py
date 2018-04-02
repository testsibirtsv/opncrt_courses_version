from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements.base import BasePageElement
from locators.checkout import CheckoutPageLocators


class CheckoutOptions(BasePageElement):

    def __init__(self, driver):
        super().__init__(driver)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CheckoutPageLocators.GUEST_ACCOUNT))

        self.guest_account = self.driver.find_element(*CheckoutPageLocators.GUEST_ACCOUNT)
        self.register_account = self.driver.find_element(*CheckoutPageLocators.REGISTER_ACCOUNT)

        self.btn_account = self.driver.find_element(*CheckoutPageLocators.BTN_ACCOUNT)
        self.btn_login = self.driver.find_element(*CheckoutPageLocators.BTN_LOGIN)

        self.email_login = self.driver.find_element(*CheckoutPageLocators.EMAIL_LOGIN)
        self.password_login = self.driver.find_element(*CheckoutPageLocators.PASSWORD_LOGIN)