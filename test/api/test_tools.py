from json import dumps

import pytest
import requests


@pytest.mark.api
def test_register_login_and_delete_user(api_client, api_valid_user_data):
    response = api_client.register(dumps(api_valid_user_data))
    assert response.status_code == requests.codes.created
    assert response.as_dict["username"] == api_valid_user_data["userName"]

    response = api_client.generate_token(dumps(api_valid_user_data))
    assert response.status_code == requests.codes.ok
    assert response.as_dict["token"] != ""

    response = api_client.delete_user()
    print(api_client.headers)
    assert response.status_code == requests.codes.ok
    assert response.as_dict["code"] == "0"


@pytest.mark.api
def test_generate_token(api_client, api_valid_user_data):
    response = api_client.generate_token(dumps(api_valid_user_data))
    assert response.status_code == requests.codes.ok
    assert response.as_dict["token"] != ""
