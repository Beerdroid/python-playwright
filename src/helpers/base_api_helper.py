from playwright.sync_api import APIRequestContext


class BaseApiHelper:
    def __init__(self, request_context: APIRequestContext) -> None:
        self.request_context = request_context
