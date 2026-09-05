import pytest

from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.regression
def test_invalid_login(login_page, test_data):
    login_page.open()

    user = test_data["invalid_user"]

    login_page.login(
        username=user["username"],
        password=user["password"]
    )

    error_message = login_page.get_error_message()

    assert "Username and password do not match" in error_message