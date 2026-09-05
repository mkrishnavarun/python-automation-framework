import pytest


@pytest.mark.ui
def test_api_ui_workflow(api_user, login_page):

    # Data came from API
    username = api_user.username

    # Open application
    login_page.open()

    # Example only:
    # login_page.enter_username(username)
    # login_page.enter_password("...")
    # login_page.click_login()

    print(f"Testing UI with user: {username}")