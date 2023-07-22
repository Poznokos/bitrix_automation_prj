

from framework.urls.base_url import BaseUrl
from framework.elements.button_element import ButtonElement
from framework.elements.field_element import FieldElement
from framework.elements.table_element import TableElement
from framework.pages.base_page import BasePage

from datetime import datetime


class ProjectManagement(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(BaseUrl().project_page_url)
        self.prj_list_table = TableElement.locator_xpath('//*[@id="SONET_GROUP_LIST_PROJECT_table"]')
        self.create_project_btn = ButtonElement.locator_id('projectAddButton')

    def create_new_project(self):
        self.create_project_btn.click()

        return CreateProjectForm(self.driver).create_project()


class CreateProjectForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.iframe = ButtonElement.locator_class_name("#iframe_fc8r4s0fdr").switch_to_frame()
        self.prj_type_workgroup = ButtonElement.locator_class_name('socialnetwork-group-create-ex__group-selector'
                                                                   '--title')
        self.next_button = ButtonElement.locator_id('sonet_group_create_popup_form_button_submit')
        self.prj_name_field = FieldElement.locator_id('GROUP_NAME_input')
        self.privacy_type_public = ButtonElement.locator_class_name('socialnetwork-group-create-ex__group-selector'
                                                                    '--description')
        self.privacy_type_private = ButtonElement.locator_class_name('socialnetwork-group-create-ex__group-selector'
                                                                     '--title')
        self.privacy_type_hidden = ButtonElement.locator_class_name('socialnetwork-group-create-ex__group-selector'
                                                                    '--description')


    def create_project(self):
        current_date_time = datetime.now()
        dt = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
        self.prj_type_workgroup.click()
        self.prj_name_field.send_keys('prj_auto_created' + dt)
        self.next_button.click()
        self.privacy_type_public.click()
        self.privacy_type_public.click()