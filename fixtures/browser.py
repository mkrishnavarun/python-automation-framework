import pytest

from drivers.driver_factory import DriverFactory


def register_options(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = DriverFactory.create_driver(
        browser=browser,
        headless=headless
    )

    yield driver

    driver.quit()