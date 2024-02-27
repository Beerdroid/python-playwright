from functools import reduce

import pytest


@pytest.mark.api
class TestApiSuite:
    def test_create_pet_via_api(self, app):
        payload = {
            "id": 0,
            "category": {"id": 0, "name": "string"},
            "name": "SuperMario",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        }

        response = app.pet_api_helper.create_pet(payload)
        assert response.ok

        json = response.json()
        assert json["name"] == payload["name"]
        assert json["category"]["id"] == 0

    def test_getting_pet_via_api(self, app):
        response = app.pet_api_helper.get_pet(9223372036854288753)
        assert response.ok

    @pytest.mark.parametrize("value,expected", [(1, 2), (2, 4), (3, 6)])
    def test_basic3(self, value, expected):
        print("result: ", value * 2)
        assert value * 2 == expected

    @pytest.mark.sandbox
    def test_basic4(self):
        arr = [4, 5, 6, 7, 9]

        mapArr = list(map(lambda a: a * 2, arr))
        print(mapArr)

        filterArr = list(filter(lambda a: a > 6, arr))
        print(filterArr)

        reduceArr = reduce(lambda acc, curr: acc + curr, arr)
        print(reduceArr)

        nextArr = next(x for x in arr if x > 8)
        print(nextArr)

        allArr = all(x > 10 for x in arr)
        print(allArr)

        anyArr = any(x == 5 for x in arr)
        print(anyArr)

        for index, item in enumerate(arr):
            print(index, item)

        for i in range(0, len(arr), 2):
            print(arr[i])
