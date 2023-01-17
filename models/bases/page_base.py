import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# this Base class is serving basic attributes for every single page inherited from Page class
from common.selectors_keys import DROP_DOWNS, ACCOUNT, ACCOUNT_OPTIONS
from models.bases.component_base import ComponentBase
from models.bases.driver_base import DriverBase


class PageBase(object):
    def __init__(self, driver: DriverBase):
        self.timeout = 30
        self.driver = driver

    def log_out(self):
        time.sleep(5)
        self.wait_element(By.CSS_SELECTOR, 'svg[testContainer="header-dropdown-arrow"]').click()
        self.wait_element(By.XPATH, "//span[contains(@class,'styles_logout')]").click()
        return self

    def select_e_memo_request_from_nav(self):
        self.wait_element(By.CSS_SELECTOR, 'a[data-event-key="req"]').click()
        return self

    def click_settings_dropdown(self):
        time.sleep(3)
        dropdowns = ComponentBase(self.driver, 'svg.rs-icon', By.CSS_SELECTOR, elements=True)
        dropdowns.create_child(1).click()
        buttons = ComponentBase(self.driver, "//div[contains(@class,'styles_menuItem')]", By.XPATH, elements=True)
        buttons.create_child(1).click()
        return self

    def click_products_dropdown_from_nav(self):
        time.sleep(5)
        # self.wait_element(By.CSS_SELECTOR, "svg[aria-label='arrow down line']").click()
        self.wait_element(By.XPATH, "//div/a[text()='Products']").click()
        return self

    def click_inventory_button_from_nav(self):
        time.sleep(3)
        self.wait_element(By.XPATH, "//*[text()='Inventory']").click()
        return self

    def click_catalogs_link_from_nav(self):
        self.wait_element(By.XPATH, "//a[text()='Catalogs']").click()
        return self

    def click_cart_icon(self):
        time.sleep(2)
        self.wait_element(By.CSS_SELECTOR, '.cart-icon').click()
        return self

    def decrease_product_quantity_in_cart(self):
        self.wait_element(By.CSS_SELECTOR, 'input[type="button"][value="-"]').click()
        return self

    def get_product_quantity_in_cart(self):
        quantity = self.wait_element(By.XPATH, '(//input[@value="-"]/../span)[1]').text
        return int(quantity)

    def click_on_checkout(self):
        self.wait_element(By.XPATH, "//*[text()='Continue to checkout']").click()
        return self

    def select_order_tab_from_nav(self):
        time.sleep(2)
        self.wait_element(By.CSS_SELECTOR, 'a[data-event-key="ord"]').click()
        return self

    def search_product(self, product):
        time.sleep(2)
        self.wait_element(By.CSS_SELECTOR, 'input[placeholder="Search"]').clear()
        self.wait_element(By.CSS_SELECTOR, 'input[placeholder="Search"]').send_keys(product)
        return self

    def wait_element(self, *locator):
        try:
            element: WebElement = WebDriverWait(self.driver.driver, 60).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()

    def wait_until_element_presence_located(self, *locator):
        try:
            element: WebElement = WebDriverWait(self.driver.driver, 60).until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()

    def click_digital_catalog_link(self):
        time.sleep(3)
        self.wait_element(By.XPATH, self.digital_catalog_link).click()
        return self

    def invisibility_of_element_located(self, *locator):
        try:
            element = WebDriverWait(self.driver.driver, 60).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT STILL VISIBLE WITHIN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()

    def element_to_be_clickable(self, *locator):
        try:
            element: WebElement = WebDriverWait(self.driver.driver, 60).until(EC.element_to_be_clickable(locator))
            return element
        except TimeoutException:
            print("\n * ELEMENT STILL NOT CLICKABLE IN GIVEN TIME! --> %s" %(locator[1]))
            self.driver.quit()