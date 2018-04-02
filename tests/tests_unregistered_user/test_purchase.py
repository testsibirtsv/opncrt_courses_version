import pytest
from selenium import webdriver

from pages.home import HomePage


class TestPurchase():

    @pytest.fixture()
    def wrap(self):
        self.driver = webdriver.Chrome()
        self.checkout_page = (HomePage(self.driver).go_to_product_id_41()
                                                   .add_to_cart()
                                                   .go_to_cart()
                                                   .go_to_checkout())
        yield
        # self.driver.close()

    def test_purchase(self, wrap):

        self.checkout_page.checkout_options()
        self.checkout_page.add_billing_details()
        # self.checkout_page.add_payment_method()
        # self.checkout_page.confirm_order()

        # order = self.checkout_page.create_order_obj()
