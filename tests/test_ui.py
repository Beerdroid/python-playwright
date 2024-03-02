import os

import allure
import pytest
from playwright.sync_api import expect

from conftest import User
from src.models.checkoutInfo import CheckoutInfo


@allure.suite("UI smoke suite")
@pytest.mark.ui
class TestUiSuite:

    @pytest.mark.smoke
    def test_ui_1(self, ui, assert_snapshot):
        ui.inventory_page.goto()
        assert_snapshot(ui.inventory_page.screenshot())

    @allure.title("Should use 2 users in a scenario")
    @pytest.mark.smoke
    def test_ui_cart(self, ui_factory, assert_snapshot):
        checkout_info = CheckoutInfo(
            first_name="John",
            last_name="Doe",
            zip_postal="5555"
        )

        mainUser = ui_factory(User.MAIN_USER)
        mainUser.inventory_page.goto()
        mainUser.inventory_page.add_item_to_cart("Sauce Labs Backpack")
        mainUser.cart_page.goto()
        mainUser.cart_page.checkout()
        mainUser.cart_page.fill_checkout_info(checkout_info)
        mainUser.cart_page.continue_checkout()
        mainUser.cart_page.finish_checkout()
        mainUser.cart_page.assert_order_completed()

        problemUser = ui_factory(User.PROBLEM_USER)
        problemUser.inventory_page.goto()
        assert_snapshot(problemUser.inventory_page.screenshot())

    @pytest.mark.skip(reason="skip mark")
    def test_ui_2(self, ui):
        pass

    @pytest.mark.xfail(reason="xfail mark")
    def test_ui_3(self, ui):
        ui.login_page.goto()
        ui.login_page.fill_credentials(
            os.environ["USER_LOGIN"], os.environ["PASSWORD"]
        )
        ui.login_page.submit_login()
        expect(ui.login_page.login_button).to_have_class(".test")

    def test_ui_4(self, ui):
        ui.login_page.goto()
        ui.login_page.fill_credentials(
            os.environ["USER_LOGIN"], os.environ["PASSWORD"]
        )
        ui.login_page.submit_login()
        expect(ui.login_page.login_button).to_have_class(".test")
