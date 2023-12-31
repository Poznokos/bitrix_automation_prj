from time import sleep

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:

    def __init__(self, locator, locator_type):
        self.locator_type = locator_type
        self.locator = locator
        self.timeout_limit = 5

    def click(self):
        self.find_element().click()

    def send_enter(self):
        self.find_element().send_keys(Keys.ENTER)

    def find_element(self, single=True, index=0):
        if single:
            self.wait_for_element()
            element = self.driver.find_element(self.locator_type, self.locator)
            return element
        else:
            element = self.driver.find_elements(self.locator_type, self.locator)[index]
            return element

    def find_elements(self):
        self.wait_for_element()
        elements = self.driver.find_elements(self.locator_type, self.locator)
        return elements

    def check_presence_of_element(self):
        wait = WebDriverWait(self.driver, self.timeout_limit)
        try:
            wait.until(EC.presence_of_element_located((self.locator_type, self.locator)))
        except TimeoutException:
            return False
        else:
            return True

    def wait_for_element(self):
        wait = WebDriverWait(self.driver, self.timeout_limit)
        element = wait.until(EC.presence_of_element_located((self.locator_type, self.locator)))
        return element

    @classmethod
    def locator_id(cls, locator):
        obj = cls(locator_type=By.ID, locator=locator)
        return obj

    @classmethod
    def locator_css(cls, locator):
        obj = cls(locator_type=By.CSS_SELECTOR, locator=locator)
        return obj

    @classmethod
    def locator_class_name(cls, locator):
        obj = cls(locator_type=By.CLASS_NAME, locator=locator)
        return obj

    @classmethod
    def locator_xpath(cls, locator):
        obj = cls(locator_type=By.XPATH, locator=locator)
        return obj

    @classmethod
    def set_element_driver(cls, driver):
        cls.driver = driver

    def move_mouse_on_element(self):
        action = webdriver.ActionChains(self.driver)
        element = self.find_element()
        action.move_to_element(element)
        action.perform()

