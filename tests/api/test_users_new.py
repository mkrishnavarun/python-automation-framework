import pytest


@pytest.mark.api
def test_get_user(user_service):

    user = user_service.get_user(1)

    assert user.id == 1
    assert user.name == "Leanne Graham"
    assert user.username == "Bret"
    assert user.email == "Sincere@april.biz"