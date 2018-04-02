import pytest
from selenium import webdriver

from pages.cart import CartPage
from pages.home import HomePage


def test_go_to_home_page():
    page = HomePage()
    page.go_to_home_page()
    assert page.is_on_home_page()


def test_empty_cart():
    cart = CartPage()
    cart.go_to_home_page().click_on_shopping_cart_tab()
    assert cart.is_cart_empty()


def test_add_to_cart():
    cart = CartPage()
    cart.go_to_home_page().click_on_phones_tab()
    cart.add_iphone_to_cart()
    assert cart.is_product_added()


def test_delete_from_cart():
    cart = CartPage()
    cart.go_to_home_page().click_on_phones_tab()
    cart.add_iphone_to_cart().delete_from_cart()
    assert cart.is_cart_empty()
