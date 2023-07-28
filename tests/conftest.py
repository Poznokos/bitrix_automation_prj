import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from framework.pages.base_page import BasePage
from framework.url_base.url_base import UrlBase


class Driver:

    def __init__(self):
        self.s = Service('/Users/poznokos/PycharmProjects/pythonProject/home/autotests/chromedriver/chromedriver')
        self.driver = webdriver.Chrome(service=self.s)
        BasePage.set_page_driver(self.driver)
        self.driver.get(UrlBase().base_url)

    def return_driver(self):
        return self.driver


@pytest.fixture(scope="function")
def main_driver():
    driver = Driver()
    instance = driver.return_driver()
    yield driver
    instance.quit()


@pytest.fixture(scope="function")
def service_driver():
    driver = Driver()
    instance = driver.return_driver()
    yield driver
    instance.quit()
