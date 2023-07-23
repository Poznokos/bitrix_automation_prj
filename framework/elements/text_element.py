from framework.elements.base_element import BaseElement


class TextElement(BaseElement):

    def get_element_text(self):
        text = self.find_element().getText()
        return text
