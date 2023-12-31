from datetime import datetime
from time import sleep
import pytest
from qaseio.pytest import qase

from framework.DataSet.user_data_set import DataSet
from framework.managers.chat_manager import word_generator
from framework.pages.base_page import BasePage
from framework.pages.chat_page import ChatPage
from framework.pages.left_side_panel import LeftSidePanel
from framework.pages.login_page import LoginPage
from framework.pages.projects_management import ProjectManagement


@qase.id(1)
@qase.title('Basic auth')
def test_basic_auth(browser):
    login_page = LoginPage()
    login_page.do_lgn_success('bitrixautouser@gmail.com', 'pLUQjnh57Q')

    assert LeftSidePanel().expand_menu_button.check_presence_of_element()


@qase.id(2)
@qase.title('Create project with default settings')
def test_create_normal_project(browser):
    current_date_time = datetime.now()
    date_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
    prj_name = 'prj_auto_created ' + date_time
    login_page = LoginPage()
    login_page.do_lgn_success('bitrixautouser@gmail.com', 'pLUQjnh57Q')
    projects_list_page = ProjectManagement()
    projects_list_page.create_new_project(prj_name)

    assert ProjectManagement().is_project_in_list(prj_name)


chat_message_text = word_generator(count=5)


@qase.id(4)
@qase.title('Receive message in chat')
def test_send_message_via_chat(receive_message_via_chat, browser):
    login_page = LoginPage()
    login_page.do_lgn_success('bitrixautousermember@gmail.com', 'pLUQjnh57Q')
    sleep(1)
    LeftSidePanel().go_to_chat_and_calls_tab()
    chat_page = ChatPage()
    chat_page.select_contact_in_chat(DataSet().admin_name)
    chat_page.send_message(chat_message_text)

    assert chat_page.is_message_in_chat(chat_message_text)


@pytest.fixture()
def receive_message_via_chat(service_browser):
    login_page = LoginPage()
    login_page.do_lgn_success('bitrixautouser@gmail.com', 'pLUQjnh57Q')
    sleep(1)
    LeftSidePanel().go_to_chat_and_calls_tab()
    chat_page = ChatPage()
    yield chat_page
    BasePage.set_page_driver(service_browser)
    chat_page.select_contact_in_chat(DataSet().user_name)
