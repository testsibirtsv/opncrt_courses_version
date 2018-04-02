"""
TODO
"""
from elements.accordion.checkoutoptions import CheckoutOptions
from elements.accordion.billingdetails import BillingDetails
from pages.base import BasePage

from faker import Faker

fake = Faker()


class CheckoutPage(BasePage):
    """
    Checkout page action methods come here
    """

    def checkout_options(self):
        """
        Fill checkout options
        """
        self.accordion = CheckoutOptions(self.driver)
        self.accordion.guest_account.click()
        self.accordion.btn_account.click()
        return self

    def checkout_options_for_registration_user(self):
        """
        Fill checkout options for registration user
        """
        self.accordion = CheckoutOptions(self.driver)
        self.accordion.email_login.send_keys('23123@gmail.com')
        self.accordion.password_login.send_keys('123123123')
        self.accordion.btn_login.click()
        return self

    def add_billing_details(self):
        """
        Fill billing details
        :return:
        """
        self.accordion = BillingDetails(self.driver)
        self.accordion.firstname.send_keys(fake.first_name())
        self.accordion.lastname.send_keys(fake.last_name())
        self.accordion.email.send_keys(fake.ascii_safe_email())
        self.accordion.telephone.send_keys(fake.phone_number())
        return self

    def add_payment_method(self):
        """
        TODO
        """

    def confirm_order(self):
        """
        TODO
        """

    def create_order_obj(self):
        """
        TODO
        """
