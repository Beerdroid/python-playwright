import os

import pytest
from playwright.sync_api import expect


@pytest.mark.ui
class TestUiSuite:
    @pytest.mark.smoke
    def test_ui(self, app):
        app.login_page.goto()
        app.login_page.fill_credentials(
            os.environ["USER_LOGIN"], os.environ["PASSWORD"]
        )
        app.login_page.submit_login()
        expect(app.login_page.login_button).to_be_hidden()

    @pytest.mark.skip(reason="skip mark")
    def test_ui2(self, app):
        app.login_page.goto()
        app.login_page.fill_credentials(
            os.environ["USER_LOGIN"], os.environ["PASSWORD"]
        )
        app.login_page.submit_login()
        expect(app.login_page.login_button).to_have_class(".test")

    @pytest.mark.xfail(reason="xfail mark")
    def test_ui23(self, app):
        app.login_page.goto()
        app.login_page.fill_credentials(
            os.environ["USER_LOGIN"], os.environ["PASSWORD"]
        )
        app.login_page.submit_login()
        expect(app.login_page.login_button).to_have_class(".test")

    def test_ui3(self, app):
        app.login_page.goto()
        app.login_page.fill_credentials(
            os.environ["USER_LOGIN"], os.environ["PASSWORD"]
        )
        app.login_page.submit_login()
        expect(app.login_page.login_button).to_have_class(".test")
