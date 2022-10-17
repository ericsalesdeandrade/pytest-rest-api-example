import pytest
from dog_api.core import DogAPI


@pytest.fixture(scope="session")
def dog_api():
    """Create DogAPI object"""
    dog_api = DogAPI()
    return dog_api
