import pytest

from pages.login_page import LoginPage


@pytest.fixture
def login_page(driver, config):
    return LoginPage(
        driver,
        config
    )