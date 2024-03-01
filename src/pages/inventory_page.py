import allure
from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.get_by_role('button', name="Add to cart")

    @allure.step("Go to inventory page")
    def goto(self):
        self.page.goto("/inventory.html")

    @allure.step("Add an item to the cart")
    def add_item_to_cart(self, item_name):
        self.page.locator(".inventory_item", has_text=item_name).locator(self.add_to_cart_button).click()