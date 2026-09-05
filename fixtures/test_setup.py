import pytest

from utils.test_data_factory import TestDataFactory


@pytest.fixture
def api_user(user_service):

    request = TestDataFactory.create_user_request()

    user = user_service.create_user(
        request.to_dict()
    )

    yield user

    user_service.delete_user(user.id)