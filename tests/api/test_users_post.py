import pytest

from api.response_validator import ResponseValidator


@pytest.mark.api
def test_get_user(api_client):

    response = api_client.get("/users/1")

    ResponseValidator.assert_status_code(
        response,
        200
    )

    ResponseValidator.assert_json_field(
        response,
        "id",
        1
    )