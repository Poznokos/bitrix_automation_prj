from framework.elements.base_element import BaseElement


class FieldElement(BaseElement):

    def send_keys(self, text):
        self.clear_field()
        self.find_element().send_keys(text)

    def clear_field(self):
        self.find_element().clear()

