import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():

    s = Service('/Users/poznokos/PycharmProjects/pythonProject/home/autotests/chromedriver/chromedriver')
    driver = webdriver.Chrome(service=s)
    yield driver
    driver.quit()