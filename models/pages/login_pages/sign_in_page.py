import time
from selenium.webdriver import Keys
from models.bases.driver_base import DriverBase
from models.bases.page_base import PageBase

class SignInPage(PageBase):
    def __init__(self, driver: DriverBase):
        super().__init__(driver)

    def write_email(self, email: str) -> 'SignInPage':
        time.sleep(5)
        self.driver.driver.find_element_by_css_selector("input[type='text']").send_keys(email)
        return self

    def write_password(self, password: str) -> 'SignInPage':
        time.sleep(3)
        self.driver.driver.find_element_by_css_selector("input[type='password']").send_keys(password)
        return self

    def click_remember_me(self) -> 'SignInPage':
        self.driver.driver.find_element_by_css_selector("input[type='checkbox']").click()
        return self

    def click_sign_in(self) -> 'SignInPage':
        self.driver.driver.find_element_by_css_selector("button[type='submit']").click()
        return self

    def write_invalid_email(self, email: str) -> 'SignInPage':
        time.sleep(3)
        self.driver.driver.find_element_by_css_selector("input[type='text']").send_keys(email)
        return self

    def write_valid_email(self, email: str) -> 'SignInPage':
        time.sleep(3)
        element = self.driver.driver.find_element_by_css_selector("input[type='text']")
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(email)
        return self

    def password(self, password: str) -> 'SignInPage':
        time.sleep(3)
        element = self.driver.driver.find_element_by_css_selector("input[type='password']")
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(password)
        return self

    def verify_email_message(self) -> 'SignInPage':
        time.sleep(3)
        msg = self.driver.driver.find_element_by_xpath("//span[contains(@class,'styles_validationMessage')]")
        print(msg.text)
        return self

    def verify_password_message(self) -> 'SignInPage':
        time.sleep(3)
        msg = self.driver.driver.find_element_by_xpath("//div[text()='Invalid Password']")
        print(msg.text)
        return self



    def page(self, SELECT_PAYMENT_METHOD, method):
        pass




