from framework.elements.button_element import ButtonElement


class FrameSwitcher:

    def __init__(self, driver):
        self.driver = driver

    def switch_to_project_creation_frame(self):
        project_creation_frame = ButtonElement.locator_css('iframe')
        iframe = project_creation_frame.find_element(single=False, index=2)
        self.driver.switch_to.frame(iframe)

    def switch_frame_to_default(self):
        self.driver.switch_to.default_content()
