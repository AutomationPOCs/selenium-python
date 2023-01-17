import random
import re
import time
import requests
from selenium.webdriver.common.by import By
from models.bases.driver_base import DriverBase
from models.bases.page_base import PageBase


class ExploreProductPage(PageBase):
    def __init__(self, driver: DriverBase):
        super().__init__(driver)

        self.first_item_in_list = "(//button[text()='Add to order'])[1]"
        self.second_item_in_list = "(//button[text()='Add to order'])[2]"
        self.order_cart = ".rs-drawer-content"
        self.cart_items = '//div[contains(@class, "CartProduct_attributes")]/..'
        self.empty_cart_msg = "//span[contains(@class,'EmptyCart')]/h3"
        self.cart_product_trash = "//span[contains(@class,'CartProduct_trash')]"
        self.no_of_items_in_cart = "//span[contains(@class,'Cart_titleWrapper')]/span"
        self.close_cart_frame = "//button[contains(@class,'header-close')]"
        self.cart_subtotal = "div[class*='RightPane_footerContainer'] > span> span > span:nth-child(2)"
        self.first_product_price = "((//b[contains(@class,'productPrice')][1]))[1]"
        self.clear_all_cart_items = "//button[text() = 'Clear all']"
        self.product_request_button = "(//button[text()='Request'])[1]"
        self.product_requested_msg = '//div[contains(@class,"styles_title")]'

    def add_first_product_in_order_cart(self) -> 'ExploreProductPage':
        self.wait_element(By.XPATH, self.first_item_in_list).click()
        return self

    def add_second_product_in_order_cart(self) -> 'ExploreProductPage':
        self.wait_element(By.XPATH, self.first_item_in_list).click()
        return self

    def verify_order_cart_is_expanded(self) -> 'ExploreProductPage':
        element_is_visible = self.wait_element(By.CSS_SELECTOR, self.order_cart).is_displayed()
        assert element_is_visible == True
        return self

    def verify_product_is_visible_in_order_cart(self) -> 'ExploreProductPage':
        cart_items = self.driver.driver.find_elements_by_xpath(self.cart_items)

        for item in cart_items:
            assert item.is_displayed() == True
        return self

    def remove_product_from_cart(self) -> 'ExploreProductPage':
        self.wait_element(By.XPATH, self.cart_product_trash).click()
        time.sleep(2)
        return self

    def verify_product_is_removed_from_cart(self) -> 'ExploreProductPage':
        msg = self.wait_element(By.XPATH, self.empty_cart_msg)
        assert msg.text == 'Your Cart Is Empty'
        return self

    def click_on_cart_button(self) -> 'ExploreProductPage':
        self.wait_element(By.XPATH, "//div[contains(@class,'cart-icon')]").click()
        return self

    def get_the_number_of_items_in_cart(self) -> 'ExploreProductPage':
        msg = self.wait_element(By.XPATH, self.no_of_items_in_cart)
        pattern = re.findall(r"[0-9]+", msg.text)
        self.number_of_cart_items = pattern[0]
        print(pattern)
        return self

    def close_the_cart(self) -> 'ExploreProductPage':
        self.wait_element(By.XPATH, self.close_cart_frame).click()
        return self

    def verify_cart_indicator_number_is_increased_by_one(self) -> 'ExploreProductPage':
        old_cart = self.number_of_cart_items
        self.get_the_number_of_items_in_cart()
        new_cart = self.number_of_cart_items
        assert new_cart > old_cart
        return self

    def verify_cart_indicator_number_is_decreased_by_one(self) -> 'ExploreProductPage':
        old_cart = self.number_of_cart_items
        self.get_the_number_of_items_in_cart()
        new_cart = self.number_of_cart_items
        assert new_cart < old_cart
        return self

    def verify_subtotal_value_is_correct(self) -> 'ExploreProductPage':
        price = self.wait_element(By.XPATH, self.first_product_price).text
        pattern = re.findall(r"[0-9]+", price)
        price = int(pattern[0])

        quantity = self.get_product_quantity_in_cart()
        print(quantity)
        print(price)
        print(quantity * price)
        # total = int(price) + int(cost)
        # pre_total = self.wait_element(By.CSS_SELECTOR, self.cart_subtotal).text
        # assert total == pre_total
        return self

    def verify_subtotal_value_after_added_one_more_product(self) -> 'ExploreProductPage':
        total = float(self.price.replace('$', ''))
        pre_total = self.wait_element(By.CSS_SELECTOR, self.cart_subtotal).text
        subtotal = float(pre_total.replace('$', ''))
        price_sum = float(total) * 2
        assert price_sum == subtotal
        return self

    def click_clear_all_button_in_cart(self) -> 'ExploreProductPage':
        self.wait_element(By.XPATH, self.clear_all_cart_items).click()
        return self

    def verify_no_items_are_present_in_cart(self) -> 'ExploreProductPage':
        msg = self.wait_element(By.XPATH, self.empty_cart_msg)
        assert msg.text == 'Your Cart Is Empty'
        return self

    def click_request_product(self) -> 'ExploreProductPage':
        self.wait_element(By.XPATH, self.product_request_button).click()
        return self

    def verify_success_message(self) -> 'ExploreProductPage':
        msg = self.wait_element(By.XPATH, self.product_requested_msg)
        assert msg.text == "Request was sent successfully"
        return self

    def generate_product_api(self, token: str) -> 'string':
        url = "https://test-server.stork.inc/products"
        productname = "Test Product " + str(random.randint(500, 5000))
        sku = "TEST" + str(random.randint(500, 5000))
        headers = {"Authorization": "Bearer " + token}
        data = {
            "data": {"title": productname, "description": "My Automation Description", "sku": sku,
                     "category": "22", "images": [
                    "http://stork-media-master.s3.amazonaws.com/ddaba9a8-c4a3-11ec-8704-127b2b5547f7.jpeg"],
                     "videos": [], "price": "123", "retail_price": "200", "reserved_price": "100",
                     "attribute_values": [{"attribute": "89", "value": 2404},
                                          {"attribute": "90", "value": "Åland Islands"},
                                          {"attribute": "91", "value": 2549}, {"attribute": "92", "value": 2432},
                                          {"attribute": "93", "value": 2436}, {"attribute": "94", "value": 4587},
                                          {"attribute": 95, "value": 4464,
                                           "children_attributes": [{"attribute": "101", "value": "1"},
                                                                   {"attribute": "110", "value": "2"},
                                                                   {"attribute": "111", "value": 2510},
                                                                   {"attribute": "112", "value": 4697},
                                                                   {"attribute": "113", "value": 2535},
                                                                   {"attribute": "114", "value": 4731},
                                                                   {"attribute": "115", "value": 4724},
                                                                   {"attribute": "116", "value": 4719},
                                                                   {"attribute": "117", "value": 2542}]},
                                          {"attribute": "96", "value": 4557}, {"attribute": "99", "value": 2488},
                                          {"attribute": "100", "value": "10"}, {"attribute": "102", "value": 4458}],
                     "is_published": True}}

        response = requests.post(url=url, json=data, headers=headers).json()
        print(response)
        return productname
