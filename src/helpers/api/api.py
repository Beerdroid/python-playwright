from src.helpers.api.pet_api_helper import PetApiHelper


class Api:
    def __init__(self, request_context):
        self.petApiHelper = PetApiHelper(request_context)
