import requests

from config.config_api import BASE_URI
from modules.api.common.api_request import APIRequest


class Client:
    __TOKEN = 'Authorization'
    userId = ""

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.base_url = BASE_URI
        self.request = APIRequest()

    def register(self, body):
        response = self.request.post(self.base_url + "/Account/v1/User", body, self.headers)
        print(response.as_dict)
        self.userId = response.as_dict["userID"]
        return response

    def generate_token(self, body):
        response = self.request.post(self.base_url + "/Account/v1/GenerateToken", body, self.headers)
        if response.status_code == requests.codes.ok:
            print(response.as_dict["token"])
            self.headers[Client.__TOKEN] = "Bearer " + response.as_dict["token"]
        return response


    def delete_user(self):
        response = self.request.delete(self.base_url + "/Account/v1/User/{id}".format(id=self.userId))
        self.userId = ""
        return response

