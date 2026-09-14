def test_framework_health(config):
    assert config.environment
    assert config.application.base_url
    assert config.api.base_url
    assert config.browser.timeout > 0
