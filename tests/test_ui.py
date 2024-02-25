import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()


@pytest.mark.ui
class TestUiSuite:

    @pytest.mark.smoke
    def test_ui(self, app):
        app.login_page.goto()
        app.login_page.fill_credentials(os.environ['USER_LOGIN'], os.environ['PASSWORD'])
        app.login_page.submit_login()
        expect(app.login_page.login_button).to_be_hidden()

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_ui2(self, app):
        app.login_page.goto()
        app.login_page.fill_credentials(os.environ['USER_LOGIN'], os.environ['PASSWORD'])
        app.login_page.submit_login()
        expect(app.login_page.login_button).to_have_class('.test')

    def test_ui2(self, app):
        app.login_page.goto()
        app.login_page.fill_credentials(os.environ['USER_LOGIN'], os.environ['PASSWORD'])
        app.login_page.submit_login()
        expect(app.login_page.login_button).to_have_class('.test')
