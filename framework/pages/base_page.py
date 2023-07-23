from framework.elements.base_element import BaseElement


class BasePage:

    def __init__(self, driver):
        BaseElement.element_driver(driver)

