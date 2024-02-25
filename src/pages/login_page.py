from playwright.sync_api import Page

from src.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.login_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

    def goto(self):
        self.page.goto('/')

    def fill_credentials(self, login, password):
        self.login_input.fill(login)
        self.password_input.fill(password)

    def submit_login(self):
        self.login_button.click()
