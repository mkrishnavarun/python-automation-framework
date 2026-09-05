from selenium import webdriver


class BrowserOptions:

    @staticmethod
    def chrome(headless: bool):
        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")

        return options

    @staticmethod
    def firefox(headless: bool):
        options = webdriver.FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        return options