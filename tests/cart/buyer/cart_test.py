import pytest
from models.pages.login_pages.sign_in_page import SignInPage
from models.pages.products.ExploreProductPage import ExploreProductPage


@pytest.mark.usefixtures("config", "setup")
class TestCart:
    def test_clear_all(self):
        try:
            # Arrange
            sign_in_page_buyer = SignInPage(driver=self.driver)
            product = ExploreProductPage(driver=self.driver)

            # Sign In as Buyer
            sign_in_page_buyer. \
                write_email(self.config.EMAIL_BUYER). \
                write_password(self.config.PASSWORD_BUYER). \
                click_sign_in()

            product.add_first_product_in_order_cart(). \
                verify_order_cart_is_expanded(). \
                click_clear_all_button_in_cart(). \
                click_cart_icon(). \
                verify_no_items_are_present_in_cart()
        finally:
            self.driver.quit()
