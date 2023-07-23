from framework.url_base.url_base import UrlBase
from framework.pages.login_page import LoginPage
from framework.pages.network_profile_page import NetworkProfilePage
from framework.pages.projects_management import ProjectManagement


def test_login_success(driver):
    driver.get('https://www.bitrix24.net/')
    login_page = LoginPage(driver)
    login_page.do_lgn_success('bitrixautouser@gmail.com', 'pLUQjnh57Q')
    network_profile_page = NetworkProfilePage(driver)

    assert network_profile_page.profile_header.check_presence_of_element()


def test_create_normal_project(driver):
    driver.get(UrlBase().base_url)
    login_page = LoginPage(driver)
    login_page.do_lgn_success('bitrixautouser@gmail.com', 'pLUQjnh57Q')
    projects_list_page = ProjectManagement(driver)
    projects_list_page.create_new_project()
