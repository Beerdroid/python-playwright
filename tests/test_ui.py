import os

import pytest
from playwright.sync_api import expect

from src.models.checkoutInfo import CheckoutInfo


@pytest.mark.ui
class TestUiSuite:
    @pytest.mark.smoke
    def test_ui_1(self, ui):
        ui.inventory_page.goto()
        ui.snapshot_helper.assert_snapshot()

    @pytest.mark.smoke
    def test_ui_cart(self, ui):
        checkout_info = CheckoutInfo(
            first_name="John",
            last_name="Doe",
            zip_postal="5555"
        )

        ui.inventory_page.goto()
        ui.inventory_page.add_item_to_cart("Sauce Labs Backpack")
        ui.cart_page.goto()
        ui.cart_page.checkout()
        ui.cart_page.fill_checkout_info(checkout_info)
        ui.cart_page.continue_checkout()
        ui.cart_page.finish_checkout()
        ui.cart_page.assert_order_completed()

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
