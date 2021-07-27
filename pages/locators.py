from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "p.price_color")

class AddToBasketLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".alertinner ")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner  p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASS_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BTN = (By.CSS_SELECTOR, "#register_form>button.btn-primary")

class BasketPageLocaors():
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    CONTENT = (By.CSS_SELECTOR, "h2.col-sm-6")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")