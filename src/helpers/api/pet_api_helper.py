from playwright.sync_api import APIRequestContext

from src.helpers.api.base_api_helper import BaseApiHelper


class PetApiHelper(BaseApiHelper):
    def __init__(self, request_context: APIRequestContext):
        super().__init__(request_context)

    def create_pet(self, payload):
        response = self.request_context.post("/v2/pet", data=payload)
        return response

    def get_pet(self, pet_id):
        response = self.request_context.post(f"/v2/pet/{pet_id}")
        return response
