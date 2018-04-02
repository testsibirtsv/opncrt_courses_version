"""
TODO
"""
from selenium.webdriver.common.by import By
from locators.base import BasePageLocators


# pylint: disable=too-few-public-methods
class CheckoutPageLocators(BasePageLocators):
    """
    TODO
    """
    ACCORDION = (By.ID, 'accrodion')

    # GUEST_ACCOUNT = (By.CSS_SELECTOR, 'input[name="account" value="guest"]')
    GUEST_ACCOUNT = (By.XPATH, '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input')

    # REGISTER_ACCOUNT = (By.CSS_SELECTOR, '[name="account" value="register"]')
    REGISTER_ACCOUNT = (By.XPATH, '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[1]/label/input')

    BTN_ACCOUNT = (By.ID, 'button-account')
    EMAIL_LOGIN = (By.ID, 'input-email')
    PASSWORD_LOGIN = (By.ID, 'input-password')
    BTN_LOGIN = (By.ID, 'button-login')

    FIRST_NAME = (By.ID, 'input-payment-firstname')
    LAST_NAME = (By.ID, 'input-payment-lastname')
    ADDRESS = (By.ID, 'input-payment-address-1')
    CITY = (By.ID, 'input-payment-city')
    POST_CODE = (By.ID, 'input-payment-postcode')
    COUNTRY = (By.ID, 'input-payment-country')
    REGION = (By.ID, 'input-payment-zone')
    EMAIL = (By.ID, 'input-payment-email')
    TELEPHONE = (By.ID, 'input-payment-telephone')
