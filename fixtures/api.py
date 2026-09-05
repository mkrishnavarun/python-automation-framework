import pytest
from api.api_client import APIClient

@pytest.fixture
def api_client(config):
    return APIClient(
        base_url=config.api.base_url,
        timeout=config.api.timeout
    )