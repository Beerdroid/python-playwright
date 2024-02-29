from playwright.sync_api import Page, expect

from src.models.checkoutInfo import CheckoutInfo


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="Checkout")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.zip_postal_input = page.locator('[data-test="postalCode"]')

    def goto(self):
        self.page.goto("/cart.html")

    def checkout(self):
        self.checkout_button.click()

    def fill_checkout_info(self, checkout_info: CheckoutInfo):
        self.first_name_input.fill(checkout_info.first_name)
        self.last_name_input.fill(checkout_info.last_name)
        self.zip_postal_input.fill(checkout_info.zip_postal)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def assert_order_completed(self):
        expect(self.page.get_by_text("Thank you for your order!")).to_be_visible()
