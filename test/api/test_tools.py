from json import dumps

import pytest
import requests


@pytest.mark.api
def test_enroll(api_client, test_user):
    response = api_client.register(dumps(test_user))
    assert response.status_code == requests.codes.ok
    assert response.as_dict["message"] == "Ok"
