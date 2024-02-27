from playwright.sync_api import Page, APIRequestContext

from src.helpers.api.pet_api_helper import PetApiHelper
from src.helpers.utils.snapshot_helper import SnapshotHelper
from src.pages.login_page import LoginPage


class App:
    def __init__(self, page: Page, request_context: APIRequestContext, assert_snapshot):
        self.login_page = LoginPage(page)
        self.pet_api_helper = PetApiHelper(request_context)
        self.snapshot_helper = SnapshotHelper(page, assert_snapshot)
