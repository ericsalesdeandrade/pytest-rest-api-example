import json
import pytest
from dog_api.core import DogAPI


def test_list_breeds(dog_api) -> None:
    """
    Unit Test to List Dog Breeds
    :param dog_api: Class Object Parameter from conftest. Type - DogAPI
    :return: None
    """
    expected_response = [
        {'weight': {'imperial': '50 - 60', 'metric': '23 - 27'},
         'height': {'imperial': '25 - 27', 'metric': '64 - 69'},
         'id': 2, 'name': 'Afghan Hound', 'country_code': 'AG',
         'bred_for': 'Coursing and hunting', 'breed_group': 'Hound',
         'life_span': '10 - 13 years',
         'temperament': 'Aloof, Clownish, Dignified, Independent, Happy',
         'origin': 'Afghanistan, Iran, Pakistan',
         'reference_image_id': 'hMyT4CDXR',
         'image': {'id': 'hMyT4CDXR', 'width': 606, 'height': 380,
                   'url': 'https://cdn2.thedogapi.com/images/hMyT4CDXR.jpg'}}]
    actual_response = dog_api.list_breeds(query_dict={"attach_breed": 1,
                                                      "page": 1, "limit": 1})
    assert actual_response == expected_response


def test_search_breeds(dog_api) -> None:
    """
    Unit Test to Search Dog Breeds
    :param dog_api: Class Object Parameter from conftest.
            Type - DogAPI
    :return: None
    """
    expected_response = [
        {'weight': {'imperial': '17 - 23', 'metric': '8 - 10'}, 'height':
            {'imperial': '13.5 - 16.5', 'metric': '34 - 42'},
         'id': 222, 'name': 'Shiba Inu',
         'bred_for': 'Hunting in the mountains of Japan, Alert Watchdog',
         'breed_group': 'Non-Sporting', 'life_span': '12 - 16 years',
         'temperament': 'Charming, Fearless, Keen, Alert, Confident, Faithful',
         'reference_image_id': 'Zn3IjPX3f'}]
    actual_response = dog_api.search_breeds(query_str="shiba")
    assert actual_response == expected_response


def test_create_vote(dog_api) -> None:
    """
    Unit Test to Vote on Dog Breed Images
    :param dog_api: Class Object Parameter from conftest. Type - DogAPI
    :return: None
    """
    expected_response = {'message': 'SUCCESS', 'id': 129143,
                         'image_id': 'asf2', 'value': 1,
                         'country_code': 'AR'}
    actual_response = dog_api.create_vote(
        payload={"image_id": "asf2", "value": 1})
    assert actual_response["message"] \
           == expected_response["message"]


def test_auth_api_key_error() -> None:
    """
    Unit Test to Test Auth on Post Request
    :return: None
    """
    dog_api_temp = DogAPI()
    dog_api_temp.headers = {
        "Content-Type": "application/json", "x-api-key": "FAKE_KEY"}
    expected_response = {"ERROR": "Authorization Error."
                                  " Please check API Key"}
    actual_response = dog_api_temp.create_vote(
        payload={"image_id": "asf2", "value": 1})
    assert json.loads(actual_response) == expected_response


def test_list_breeds_wrong_arg_type_value_error(dog_api) -> None:
    with pytest.raises(ValueError):
        actual_response = dog_api.list_breeds(
            query_dict="Invalid")


def test_create_vote_wrong_arg_type_value_error(dog_api) -> None:
    with pytest.raises(ValueError):
        actual_response = dog_api.create_vote(
            payload="Invalid")


def test_create_vote_wrong_payload_value_error(dog_api) -> None:
    with pytest.raises(ValueError):
        actual_response = dog_api.create_vote(
            payload={"image_id": "xyz"})
