from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url.find("login") != -1, "this is not login page"

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert True, "There is no LogIn form"

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        assert True, "There is no Registration form"

    def register_new_user(self, email, password):
        email_user = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_user.send_keys(email)
        pass_user = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS)
        pass_user.send_keys(password)
        pass_user_conf = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_CONFIRM)
        pass_user_conf.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        btn.click()