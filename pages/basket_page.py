from .base_page import BasePage
from .locators import BasketPageLocaors

class BasketPage(BasePage):
    def should_be_empty(self):
        text = self.browser.find_element(*BasketPageLocaors.BASKET_IS_EMPTY).text
        assert "Your basket is empty." in text, "message should be Your basket is empty, but it's wrong"

    def guest_should_not_seen_products(self):
        self.is_not_element_present(*BasketPageLocaors.CONTENT)
        assert True, "products in the basket, but shouldn't!"