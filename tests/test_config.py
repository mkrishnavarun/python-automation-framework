from config.config_loader import ConfigLoader


def test_load_qa_config():
    config = ConfigLoader.load("qa")

    assert config.environment == "qa"
    assert config.application.base_url == (
        "https://www.saucedemo.com"
    )