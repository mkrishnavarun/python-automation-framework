from utils.json_reader import JsonReader


def test_read_user_data():
    data = JsonReader.read("test_data/users.json")

    assert data["valid_user"]["username"] == "standard_user"