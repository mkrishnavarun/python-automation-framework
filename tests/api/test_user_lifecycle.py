import pytest

from models.create_user_request import CreateUserRequest


@pytest.mark.api
def test_create_user(user_service):

    request = CreateUserRequest(
        name="Automation User",
        username="automation_user",
        email="automation@test.com"
    )

    user = user_service.create_user(
        request.to_dict()
    )


    assert user.name == "Automation User"
    assert user.username == "automation_user"
    assert user.email == "automation@test.com"