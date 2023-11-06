import pytest

from modules.api.clients.client import Client


@pytest.fixture
def test_user():
    return {"first_name": "Testname", "last_name": "Testlastname", "city": "Kyiv", "email": "testmail@test.com",
            "mobile": "0934459084"}


@pytest.fixture
def api_client():
    return Client()


@pytest.fixture
def api_valid_user_data():
    return {"firstName": "Testname", "lastName": "Testlastname", "city": "Kyiv", "email": "testmail@test.com",
            "mobile": "0934459084", "country": "40", "code": "2z3x"}
