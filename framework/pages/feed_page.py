from framework.elements.base_element import BaseElement
from framework.pages.base_page import BasePage


class FeedPage(BasePage):

    def __init__(self):
        super().__init__()
        self.portal_logo = BaseElement.locator_class_name('logo-text-container')