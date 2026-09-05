from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from config.models import EnvironmentConfig


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver, config:EnvironmentConfig):
        # timeout = config["browser"]["timeout"]
        timeout = config.browser.timeout
        super().__init__(driver, timeout=timeout)
        self.config = config

    def open(self):
        self.logger.info("Opening login page")
        # base_url = self.config["application"]["base_url"]
        base_url = self.config.application.base_url
        self.driver.get(base_url)

    def enter_username(self, username: str):
        self.logger.info("Entering username")
        self.type(self.USERNAME, username)

    def enter_password(self, password: str):
        self.logger.info("Entering password")
        self.type(self.PASSWORD, password)

    def click_login(self):
        self.logger.info("Clicking login button")
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        self.logger.info("Performing login")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self) -> bool:
        return "inventory" in self.driver.current_url

    def get_error_message(self) -> str:
        return self.find_element(
            (By.CSS_SELECTOR, "[data-test='error']")
        ).text