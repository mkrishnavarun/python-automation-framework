from selenium import webdriver

from drivers.browser_options import BrowserOptions


class DriverFactory:

    @staticmethod
    def create_driver(
        browser: str = "chrome",
        headless: bool = False
    ):
        browser = browser.lower()

        if browser == "chrome":
            return webdriver.Chrome(
                options=BrowserOptions.chrome(headless)
            )

        if browser == "firefox":
            return webdriver.Firefox(
                options=BrowserOptions.firefox(headless)
            )

        raise ValueError(
            f"Unsupported browser: {browser}"
        )