# ruff: noqa: F401
from pathlib import Path

import pytest

from config.config_loader import ConfigLoader
from drivers.driver_factory import DriverFactory
from fixtures.api import api_client
from fixtures.browser import driver
from fixtures.browser import (
    register_options as register_browser_options,
)
from fixtures.config import config
from fixtures.config import (
    register_options as register_config_options,
)
from fixtures.data import test_data
from fixtures.pages import login_page
from fixtures.services import user_service
from fixtures.test_setup import api_user
from pages.login_page import LoginPage
from utils.json_reader import JsonReader
from utils.logger import get_logger

logger = get_logger("conftest.pt")

# @pytest.fixture(scope="session")
# def test_data():
#     return JsonReader.read("test_data/users.json")


@pytest.fixture
def test_user():
    print("\nSETUP: Creating test user")

    user = {"username": "test_user", "password": "password123"}

    yield user

    print("\nTEARDOWN: Cleaning up test user")


# @pytest.fixture
# def driver(request):
#     browser_name = request.config.getoption("--browser")
#     headless = request.config.getoption("--headless")
#
#     browser = DriverFactory.create_driver(
#         browser=browser_name,
#         headless=headless
#     )
#
#     yield browser
#
#     browser.quit()

# def pytest_addoption(parser):
#     parser.addoption(
#         "--env",
#         action="store",
#         default="qa",
#         help="Environment to run tests against"
#     )
#
#     parser.addoption(
#         "--headless",
#         "--browser",
#         action="store",
#         default="chrome",
#         help="Browser to use for test execution"
#     )

# @pytest.fixture(scope="session")
# def config(request):
#     environment = request.config.getoption("--env")
#
#     return ConfigLoader.load(environment)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    browser = item.funcargs.get("driver")

    if browser is None:
        return

    screenshot_dir = Path("reports/screenshots")
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    test_name = item.nodeid.replace("/", "_").replace("::", "_")
    screenshot_path = screenshot_dir / f"{test_name}.png"

    browser.save_screenshot(str(screenshot_path))

    logger.error(
        "Test failed: %s. Screenshot: %s",
        item.nodeid,
        screenshot_path,
    )


def pytest_addoption(parser):
    register_config_options(parser)
    register_browser_options(parser)


# @pytest.fixture
# def login_page(driver, config):
#     return LoginPage(driver, config)
