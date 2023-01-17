from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class DriverBase:
    def __init__(self, chrome_url: str, url: str):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        options.add_argument('--window-size=1920,1080')
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        chrome_file = chrome_url if chrome_url else ChromeDriverManager().install()
        self.driver = webdriver.Chrome(chrome_file)
        self.headless = True
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.refresh()


    def quit(self):
        self.driver.quit()

    def getPageSource(self):
        pass

