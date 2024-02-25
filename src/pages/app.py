from playwright.sync_api import Page, APIRequestContext

from src.helpers.pet_api_helper import PetApiHelper
from src.pages.login_page import LoginPage


class App:
    def __init__(self, page: Page, request_context: APIRequestContext):
        self.login_page = LoginPage(page)
        self.pet_api_helper = PetApiHelper(request_context)
