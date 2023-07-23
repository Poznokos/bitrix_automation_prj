from time import sleep

from framework.elements.button_element import ButtonElement
from framework.elements.field_element import FieldElement
from framework.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_field = FieldElement.locator_id('login')
        self.password_field = FieldElement.locator_id('password')
        self.next_button = ButtonElement.locator_xpath('//*[@data-action="submit"]')

    def do_lgn_success(self, user_name, user_pwd):
        self.login_field.send_keys(user_name)
        sleep(0.1)  # need to be fixed
        self.next_button.click()
        self.password_field.send_keys(user_pwd)
        self.next_button.click()

    def do_lgn_fail(self, user_name, user_pwd):
        self.login_field.send_keys(user_name)
        sleep(0.1)  # need to be fixed
        self.next_button.click()
        self.password_field.send_keys(user_pwd)
        self.next_button.click()

    def reset_pwd(self):
        pass
