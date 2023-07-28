from framework.elements.base_element import BaseElement
from framework.elements.button_element import ButtonElement
from framework.pages.base_page import BasePage


class LeftSidePanel(BasePage):

    def __init__(self):
        super().__init__()
        self.expand_menu_button = ButtonElement.locator_xpath('//*[@id="header-inner"]//*[@class="menu-switcher"]')
        self.expand_menu_button.move_mouse_on_element()
        self.chat_and_calls_button = ButtonElement.locator_xpath('//*[@id="bx_left_menu_menu_im_messenger"]')

    def go_to_chat_and_calls_tab(self):
        self.chat_and_calls_button.click()

