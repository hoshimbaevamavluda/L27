from data import url_text_box_page
from pages_demoqa.base_page import BasePage


class TextBox(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.full_name = "#userName"
        self.input_full_name = self.page.locator(self.full_name)
        self.email = "#userEmail"
        self.input_email = self.page.locator(self.email)
        self.label_address = self.page.locator("#currentAddress-label")


    def open_page(self):
        self.page.goto(f"{url_text_box_page}")

    def fill_full_name(self, text):
        self.input_full_name.fill(text)

    def fill_email(self, text):
        self.input_email.fill(text)

    def input_value_name(self):
        return self.input_full_name.input_value()

    def input_value_email(self):
        return self.input_email.input_value()

    def inner_text_address(self):
        return self.label_address.inner_text()

    def text_content_address(self):
        return self.label_address.text_content()
