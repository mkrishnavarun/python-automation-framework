from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.logger import get_logger


class BasePage:

    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)

    def find_element(self, locator: Tuple):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator: Tuple):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator: Tuple, text: str):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)