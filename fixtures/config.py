import pytest

from config.config_loader import ConfigLoader


def register_options(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against"
    )


@pytest.fixture(scope="session")
def config(request):
    environment = request.config.getoption("--env")

    return ConfigLoader.load(environment)