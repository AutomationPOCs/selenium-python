import time
from copy import copy
from email.mime import text

from retry.api import retry_call
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from models.bases.driver_base import DriverBase


class ComponentBase:
    def __init__(self, driver: DriverBase, class_name: str, by: By = By.CLASS_NAME, elements: bool = False):
        self.driver = driver.driver
        self.class_name = class_name
        self.by = by
        time.sleep(2)

        if elements:
            retry_call(f=self.find_elements, exceptions=NoSuchElementException, tries=30)
        else:
            retry_call(f=self.find_element, exceptions=NoSuchElementException, tries=30)

    def find_elements(self):
        self.component = self.driver.find_elements(self.by, self.class_name)
        if len(self.component) == 0:
            raise NoSuchElementException()

    def find_element(self):
        self.component = self.driver.find_element(self.by, self.class_name)

    def create_child(self, place: int):
        child = copy(self)
        self.place = place
        child.component = self.component[place]
        return child

    def write(self, content: str):
        self.click()
        ActionChains(self.driver).move_to_element(self.component).send_keys(content).perform()

    def delete_all(self):
        ActionChains(self.driver).move_to_element(self.component).key_down(Keys.CONTROL).send_keys("a").\
            key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()

    def click(self):
        ActionChains(self.driver).move_to_element(self.component).click(self.component).perform()

    def get_text(self) -> str:
        return self.component.text

    def send_keys(self, value: str):
        self.component = self.driver.find_element(self.by, self.class_name).send_keys(value)

    def clear(self):
        pass


