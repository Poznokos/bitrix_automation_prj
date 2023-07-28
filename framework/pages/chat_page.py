from framework.elements.button_element import ButtonElement
from framework.elements.field_element import FieldElement
from framework.elements.text_element import TextElement
from framework.managers.chat_manager import word_generator
from framework.pages.base_page import BasePage


class ChatPage(BasePage):

    def __init__(self):
        self.text_chat_tab = ButtonElement.locator_xpath('//*[@id="bx-desktop-tab-im"]')
        self.chat_search_field = FieldElement.locator_xpath('//*[@id="bx-desktop-tab-content-im"]//*['
                                                            '@class="bx-messenger-input"]')
        self.contacts_search_results_list = TextElement.locator_xpath('//*[@class="bx-messenger-search-result-section'
                                                                      '-wrapper"][1]//*['
                                                                      '@class="bx-im-component-chat-name-text- '
                                                                      'bx-im-component-chat-name-text"]')
        self.message_input_field = FieldElement.locator_xpath('//*[@class="bx-messenger-textarea-input"]')
        self.messages_list_text = TextElement.locator_xpath("//*[@class='bx-messenger-content-item-text-wrap ']//*["
                                                      "contains(@id,'im-message-')]")

    def select_contact_in_chat(self, contact_type):
        self.chat_search_field.click()
        self.chat_search_field.send_keys(contact_type)
        contacts_list = self.contacts_search_results_list.find_elements()
        for contact in contacts_list:
            contact_name_text = contact.text
            if contact_name_text == contact_type:
                contact.click()

    def send_message(self, words_count):
        message = word_generator(words_count)
        self.message_input_field.send_keys(message)
        self.message_input_field.send_enter()
        return message

    def is_message_in_chat(self, sent_message):
        messages_list = self.messages_list_text.find_elements()
        for message in messages_list:
            message_text = message.text
            if message_text == sent_message:
                return True
            else:
                return False

