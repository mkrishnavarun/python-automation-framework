import pytest

from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_valid_login(driver, config, test_data):

    login_page = LoginPage(driver, config)

    login_page.open()

    user = test_data["valid_user"]

    login_page.enter_username(user["username"])
    login_page.enter_password(user["password"])
    login_page.click_login()

    assert login_page.is_login_successful()