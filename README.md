# PyTest REST API Example

This project explains how to call an External Rest API ([DogAPI](https://thedogapi.com/)) and validate call `GET` and `POST` API methods using PytTest including the use of fixtures and mocking.
# Requirements
* Python (3.10.6)

Please install the dependencies via the `requirements.txt` file using 
```commandline
pip install -r requirements.txt
```
If you don't have Pip installed please follow instructions online on how to do it.   

# Repo Structure
The repo structure is very simple with just one source code folder `dog_api` containing the source code in file `core.py`.

The Unit Tests are located under `/tests` including the file `conftest.py`. The Unit tests are split across 2 files - `test_dog_api_core_basic.py` and `test_dog_api_core_mock.py`

# How To Run the Unit Tests
To run the Unit Tests, from the root of the repo run
```commandline
pytest ./tests/unit/
```

If you have any questions about the project please raise an Issue on GitHub. 