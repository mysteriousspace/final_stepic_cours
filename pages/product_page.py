from .base_page import BasePage
from .locators import ProductPageLocators, AddToBasketLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        link.click()

    def should_be_message_product_in_basket(self):
        text_box = self.browser.find_element(*AddToBasketLocators.PRODUCT_IN_BASKET)
        text = text_box.text
        product_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        assert text == product_name + " has been added to your basket.", "right product wasn't beemn added in basket"

    def should_be_right_price_in_basket(self):
        price_in_basket = self.browser.find_element(*AddToBasketLocators.PRICE_IN_BASKET).text
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        assert price_in_basket == price_of_product, "price of product != price in basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*AddToBasketLocators.PRODUCT_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_dissapear_message(self):
        assert self.is_disappeared(*AddToBasketLocators.PRODUCT_IN_BASKET), \
            "Success message is dissapeared, but should not to dissapear"