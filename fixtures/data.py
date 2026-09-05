import pytest

from utils.json_reader import JsonReader


@pytest.fixture(scope="session")
def test_data():
    return JsonReader.read(
        "test_data/users.json"
    )