import pytest

@pytest.mark.smoke
def test_framework_is_working(test_user):
    assert test_user["username"] == "test_user"
