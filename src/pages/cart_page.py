import allure
from playwright.sync_api import Page, expect

from src.models.checkoutInfo import CheckoutInfo
from src.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.zip_postal_input = page.locator('[data-test="postalCode"]')

    @allure.step("Go to the cart page")
    def goto(self):
        self.page.goto("/cart.html")

    @allure.step("Checkout the cart page")
    def checkout(self):
        self.checkout_button.click()

    @allure.step("Fill checkout form")
    def fill_checkout_info(self, checkout_info: CheckoutInfo):
        self.first_name_input.fill(checkout_info.first_name)
        self.last_name_input.fill(checkout_info.last_name)
        self.zip_postal_input.fill(checkout_info.zip_postal)

    @allure.step("Continue checkout")
    def continue_checkout(self):
        self.continue_button.click()

    @allure.step("Finish checkout")
    def finish_checkout(self):
        self.finish_button.click()

    @allure.step("Assert order is completed successfully")
    def assert_order_completed(self):
        expect(self.page.get_by_text("Thank you for your order!")).to_be_visible()
