from framework.elements.text_element import TextElement
from framework.pages.base_page import BasePage


class NetworkProfilePage(BasePage):

    def __init__(self):
        super().__init__()
        self.profile_header = TextElement.locator_class_name('b24network-account-header-title-pass')