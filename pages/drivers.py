from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class Drivers:
    def __init__(self, browser="chrome"):
        self.browser = browser.lower()
        self.driver = self._init_driver()

    def _init_driver(self):
        if self.browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--headless")  # Run in headless mode for CI/CD
            service = ChromeService(ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=options)

        elif self.browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")  # Run in headless mode for CI/CD
            service = FirefoxService(GeckoDriverManager().install())
            return webdriver.Firefox(service=service, options=options)

        else:
            raise ValueError("Unsupported browser: Use 'chrome' or 'firefox'")

    def quit(self):
        self.driver.quit()
