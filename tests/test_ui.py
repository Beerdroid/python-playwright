import os

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
class TestUiSuite:
    @pytest.mark.smoke
    def test_ui_1(self, ui):
        ui.login_page.page.goto("/inventory.html")
        ui.snapshot_helper.assert_snapshot()

    @pytest.mark.skip(reason="skip mark")
    def test_ui_2(self, ui):
        ui.login_page.page.goto("/inventory.html")
        expect(ui.login_page.login_button).to_have_class(".test")

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
