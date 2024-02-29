from playwright.sync_api import Page

from src.helpers.utils.snapshot_helper import SnapshotHelper
from src.pages.login_page import LoginPage


class Ui:
    def __init__(self, page: Page, assert_snapshot):
        self.login_page = LoginPage(page)
        self.snapshot_helper = SnapshotHelper(page, assert_snapshot)
