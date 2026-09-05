import pytest


@pytest.mark.api
def test_get_user(api_client):

    response = api_client.get("/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1