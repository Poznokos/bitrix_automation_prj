from framework.elements.base_element import BaseElement


class BasePage:

    def __init__(self, driver):
        BaseElement.element_driver(driver)
        type(self).bar = property(self.get_bar)

    def get_bar(self):
        return "https://poznokosme.bitrix24.eu/"