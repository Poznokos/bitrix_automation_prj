from framework.elements.base_element import BaseElement


class FieldElement(BaseElement):

    def send_keys(self, text):
        self.find_element().send_keys(text)

