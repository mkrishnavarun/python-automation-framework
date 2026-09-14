from selenium import webdriver

from drivers.browser_options import BrowserOptions
from exceptions import FrameworkError, UnsupportedBrowserError

class DriverFactory:
    @staticmethod
    def create_driver(browser: str = "chrome", headless: bool = False):
        browser = browser.lower()
        try:
            if browser == "chrome":
                return webdriver.Chrome(options=BrowserOptions.chrome(headless))

            if browser == "firefox":
                return webdriver.Firefox(options=BrowserOptions.firefox(headless))

            raise ValueError(f"Unsupported browser: {browser}")

        except UnsupportedBrowserError:
            raise

        except Exception as exc:
            raise FrameworkError(
                f"Failed to create {browser} WebDriver: {exc}"
            ) from exc
