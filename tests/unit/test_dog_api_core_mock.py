import json
import requests_mock
from dog_api.core import DogAPI


def test_mock_list_breeds(dog_api) -> None:
    expected_mock_response = [{'weight': {'imperial': '50 - 60', 'metric': '23 - 27'},
                               'height': {'imperial': '25 - 27', 'metric': '64 - 69'},
                               'id': 2, 'name': 'Afghan Hound', 'country_code': 'AG',
                               'bred_for': 'Coursing and hunting', 'breed_group': 'Hound',
                               'life_span': '10 - 13 years',
                               'temperament': 'Aloof, Clownish, Dignified, Independent, Happy',
                               'origin': 'Afghanistan, Iran, Pakistan', 'reference_image_id': 'hMyT4CDXR',
                               'image': {'id': 'hMyT4CDXR', 'width': 606, 'height': 380,
                                         'url': 'https://cdn2.thedogapi.com/images/hMyT4CDXR.jpg'}}]
    mock_address = "https://api.test.com/"

    with requests_mock.Mocker() as rm:
        rm.get(mock_address, json=expected_mock_response, status_code=200)
        actual_mock_response = dog_api.list_breeds(query_dict={"attach_breed": 1, "page": 1, "limit": 1})
        assert actual_mock_response == expected_mock_response
