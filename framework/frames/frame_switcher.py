from framework.elements.button_element import ButtonElement


def switch_to_project_creation_frame():
    project_creation_frame = ButtonElement.locator_css('iframe')
    project_creation_frame.switch_frame_to_custom()
