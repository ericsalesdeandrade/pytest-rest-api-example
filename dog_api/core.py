import logging
from enum import Enum

from requests.auth import HTTPBasicAuth
import requests
import os

# Set Logging
logging.basicConfig(level=logging.INFO)


class RequestType(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class DogAPI:
    def __init__(self):
        api_key = os.environ.get("API_KEY")
        self.headers = {"Content-Type": "application/json", "x-api-key": api_key}
        self.auth = HTTPBasicAuth("apikey", api_key)
        self.base_url = "https://api.thedogapi.com/v1"

    def call_api(self, request_type: str, endpoint: str, payload: dict | str = None) -> str:
        try:
            response = ""
            if request_type == "GET":
                response = requests.get(endpoint, auth=self.auth, timeout=30,
                                        params=payload)
            elif request_type == "POST":
                response = requests.post(endpoint, headers=self.headers, auth=self.auth, timeout=30,
                                         json=payload)

            response.raise_for_status()
            if response.status_code in (200, 201):
                return response.json()
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    def list_breeds(self, query_dict: dict):
        breeds_url = f"{self.base_url}/breeds"
        response = self.call_api(request_type=RequestType.GET.value, endpoint=breeds_url, payload=query_dict)
        return response

    def search_breeds(self, query_str: str):
        search_breeds_url = f"{self.base_url}/breeds/search"
        response = self.call_api(request_type=RequestType.GET.value, endpoint=search_breeds_url,
                                 payload={"q": query_str})
        return response

    def create_vote(self, payload: dict):
        create_vote_url = f"{self.base_url}/votes"
        response = self.call_api(request_type=RequestType.POST.value, endpoint=create_vote_url,
                                 payload=payload)
        return response


if __name__ == "__main__":
    dog = DogAPI()
    list_breeds_resp = dog.list_breeds(query_dict={"attach_breed": 1, "page": 1, "limit": 1})
    search_breeds_resp = dog.search_breeds(query_str="shiba")
    create_vote_resp = dog.create_vote(payload={"image_id": "asf2", "value": 1})
    print(list_breeds_resp)
    print(search_breeds_resp)
    print(create_vote_resp)
