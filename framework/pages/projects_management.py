from framework.frames.frame_switcher import FrameSwitcher
from framework.url_base.url_base import UrlBase
from framework.elements.button_element import ButtonElement
from framework.elements.field_element import FieldElement
from framework.elements.table_element import TableElement
from framework.pages.base_page import BasePage

from datetime import datetime


class ProjectManagement(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(UrlBase().base_url + 'company/personal/user/1/tasks/projects/')
        self.prj_list_table = TableElement.locator_xpath('//*[@id="SONET_GROUP_LIST_PROJECT_table"]')
        self.create_project_btn = ButtonElement.locator_id('projectAddButton')

    def create_new_project(self):
        self.create_project_btn.click()
        return CreateProjectForm(self.driver).create_project()


class CreateProjectForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        FrameSwitcher(self.driver).switch_to_project_creation_frame()
        self.prj_type_project = ButtonElement.locator_xpath(
            '//*[@id="sonet_group_create_popup_form"]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]')
        self.prj_type_workgroup = ButtonElement.locator_xpath(
            '//*[@id="sonet_group_create_popup_form"]/div[1]/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]')
        self.next_button = ButtonElement.locator_id('sonet_group_create_popup_form_button_submit')
        self.prj_name_field = FieldElement.locator_id('GROUP_NAME_input')
        self.privacy_type_public = ButtonElement.locator_class_name('socialnetwork-group-create-ex__group-selector'
                                                                    '--description')
        self.privacy_type_private = ButtonElement.locator_xpath('//*[@id="sonet_group_create_popup_form"]/div[1]/div[1]/div[3]/div[4]/div[3]/div[2]/div[2]/div[1]')
        self.privacy_type_hidden = ButtonElement.locator_class_name('socialnetwork-group-create-ex__group-selector'
                                                                    '--description')

    def create_project(self):
        current_date_time = datetime.now()
        date_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
        self.prj_type_project.click()
        self.next_button.click()
        self.prj_name_field.send_keys('prj_auto_created' + date_time)
        self.next_button.click()
        self.privacy_type_private.click()
        self.next_button.click()
        self.next_button.click()
