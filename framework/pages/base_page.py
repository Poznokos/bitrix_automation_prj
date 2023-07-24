from framework.elements.base_element import BaseElement
from framework.frames.frame_switcher import FrameSwitcher


class BasePage:

    @classmethod
    def set_page_driver(cls, driver):
        cls.driver = driver
        BaseElement.set_element_driver(driver)
        FrameSwitcher.set_iframe_driver(driver)
