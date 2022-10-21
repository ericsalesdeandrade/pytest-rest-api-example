import json
import logging
from enum import Enum
import requests
import os

# Set Logging
logging.basicConfig(level=logging.INFO)


class RequestType(Enum):
    """
    Enum class for RequestType containing 4 values - GET, POST, PUT, PATCH, DELETE
    """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class DogAPI:
    def __init__(self):
        """
        Function to initialise the Dog API Class
        """
        api_key = os.environ.get("API_KEY")
        self.headers = {"Content-Type": "application/json",
                        "x-api-key": api_key}
        self.base_url = "https://api.thedogapi.com/v1"

    def call_api(self, request_type: str, endpoint: str,
                 payload: dict | str = None) -> str:
        """
        Function to call the API via the Requests Library
        :param request_type: Type of Request.
               Supported Values - GET, POST, PUT, PATCH, DELETE.
               Type - String
        :param endpoint: API Endpoint. Type - String
        :param payload: API Request Parameters or Query String.
               Type - String or Dict
        :return: Response. Type - JSON Formatted String
        """
        try:
            response = ""
            if request_type == "GET":
                response = requests.get(endpoint, timeout=30,
                                        params=payload)
            elif request_type == "POST":
                response = requests.post(endpoint, headers=self.headers,
                                         timeout=30, json=payload)

            if response.status_code in (200, 201):
                return response.json()
            elif response.status_code == 401:
                return json.dumps({"ERROR": "Authorization Error. "
                                            "Please check API Key"})
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            logging.error(errh)
        except requests.exceptions.ConnectionError as errc:
            logging.error(errc)
        except requests.exceptions.Timeout as errt:
            logging.error(errt)
        except requests.exceptions.RequestException as err:
            logging.error(err)

    def list_breeds(self, query_dict: dict) -> str:
        """
        Function to List Dog Breeds -
        https://docs.thedogapi.com/api-reference/breeds/breeds-list
        :param query_dict: Query String Parameters. Type - Dict
        :return: Response. Type - JSON Formatted String
        """
        breeds_url = f"{self.base_url}/breeds"
        if isinstance(query_dict, dict):
            response = self.call_api(request_type=RequestType.GET.value,
                                     endpoint=breeds_url, payload=query_dict)
        else:
            raise ValueError("ERROR - Parameter 'query_dict' should be of Type Dict")
        return response

    def search_breeds(self, query_str: str):
        """
        Function to Search Dog Breeds
        - https://docs.thedogapi.com/api-reference/breeds/breeds-search
        :param query_str: Query String. Type - String
        :return: Response. Type - JSON Formatted String
        """
        search_breeds_url = f"{self.base_url}/breeds/search"
        if isinstance(query_str, str):
            response = self.call_api(request_type=RequestType.GET.value,
                                     endpoint=search_breeds_url,
                                     payload={"q": query_str})
        else:
            raise ValueError("ERROR - Parameter 'query_str' should be of Type Str")
        return response

    def create_vote(self, payload: dict) -> str:
        """
        Function to Vote on Dog Image
        - https://docs.thedogapi.com/api-reference/votes/votes-post
        :param payload: API Request Parameters. Type - Dict
        :return: Response. Type - JSON Formatted String
        """
        create_vote_url = f"{self.base_url}/votes"
        if isinstance(payload, dict) and "image_id" and "value" in payload:
            response = self.call_api(request_type=RequestType.POST.value,
                                     endpoint=create_vote_url,
                                     payload=payload)
        else:
            raise ValueError("ERROR - Parameter 'payload' should be of Type Dict")
        return response
