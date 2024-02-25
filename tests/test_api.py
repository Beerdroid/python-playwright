import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.api
class TestApiSuite:

    def test_create_pet_via_api(self, app):
        payload = {
            "id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "SuperMario",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }

        response = app.pet_api_helper.create_pet(payload)
        assert response.ok

    def test_getting_pet_via_api(self, app):
        response = app.pet_api_helper.get_pet(9223372036854288753)
        assert response.ok

    @pytest.mark.parametrize("value,expected", [(1, 2), (2, 4), (3, 6)])
    def test_basic3(self, value, expected):
        print('result: ', value * 2)
        assert value * 2 == expected
