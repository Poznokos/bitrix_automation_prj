from datetime import datetime

import config
from utils.mongo_manager.mongo_manager import MongoManager
from framework.pages.base_page import BasePage
from data.url_base.url_base import UrlBase

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import json


@pytest.fixture(scope='session', autouse=True)
def backup_tests_results():
    db_name = 'test_results_db'
    current_date_time = datetime.now()
    db_collection_name = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
    yield
    qase_report = open('build/qase-report/report.json')
    json_content = [json.load(qase_report)]

    mongo_db = MongoManager()
    mongo_db.insert_data(db_name, db_collection_name, json_content)


class Driver:

    def __init__(self, options, selenium_address):
        self.options = options
        self.selenium_address = selenium_address
        self.options.add_argument('--allow-insecure-localhost')
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Remote(self.selenium_address, options=self.options)
        BasePage.set_page_driver(self.driver)
        self.driver.get(UrlBase().base_url)

    @classmethod
    def browser_chrome(cls):
        obj = cls(options=ChromeOptions(), selenium_address=config.selenium_chrome_host)
        return obj

    @classmethod
    def browser_firefox(cls):
        obj = cls(options=FirefoxOptions(), selenium_address=config.selenium_firefox_host)
        return obj

    def check_selenium_server_available(self):
        try:
            session = requests.Session()
            retry = Retry(connect=3, backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)

            session.get(self.selenium_address)
        except ConnectionError as e:
            print(e)

    def start_browser(self):
        self.check_selenium_server_available()
        return self.driver


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def browser(request):
    if request.param == "chrome":
        main_driver = Driver.browser_chrome()
        main_instance = main_driver.start_browser()
        yield main_instance
        main_instance.quit()
    if request.param == "firefox":
        main_driver = Driver.browser_firefox()
        main_instance = main_driver.start_browser()
        yield main_instance
        main_instance.quit()


@pytest.fixture(scope="function")
def service_browser():
    service_driver = Driver.browser_chrome()
    service_instance = service_driver.start_browser()
    yield service_instance
    service_instance.quit()
