import requests

from config.config_api import BASE_URI
from modules.api.common.api_request import APIRequest


class Client:
    __TOKEN = 'token'

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.base_url = BASE_URI
        self.request = APIRequest()

    # Send request of authorization on server
    def register(self, body):
        response = self.request.post(self.base_url + "register", body, self.headers)
        return response

