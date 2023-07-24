import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from framework.pages.base_page import BasePage


@pytest.fixture(scope="function")
def driver():

    s = Service('/Users/poznokos/PycharmProjects/pythonProject/home/autotests/chromedriver/chromedriver')
    driver = webdriver.Chrome(service=s)
    BasePage.set_page_driver(driver)
    yield driver
    driver.quit()
