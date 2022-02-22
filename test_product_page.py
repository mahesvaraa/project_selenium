from time import sleep

import pytest

from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


class TestUser:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer9"
        page = ProductPage(browser, url)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register()
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/'
        page = ProductPage(browser, url)
        page.open()
        page.get_product_name()
        page.add_to_basket_button()
        page.go_to_the_basket()
        page = BasketPage(browser, url)
        page.product_is_exist_in_basket()
        sleep(2)


class TestGuest:

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        url = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/'
        page = BasePage(browser, url)
        page.open()
        page.go_to_the_basket()
        page = BasketPage(browser, browser.current_url)
        page.check_empty_basket()
        sleep(2)

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        url = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/'
        page = ProductPage(browser, url)
        page.open()
        page.get_product_name()
        page.add_to_basket_button()
        page.go_to_the_basket()
        page = BasketPage(browser, url)
        page.product_is_exist_in_basket()
        sleep(2)

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        url = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/'
        page = ProductPage(browser, url)
        page.open()
        page.go_to_login_page()
        sleep(2)
