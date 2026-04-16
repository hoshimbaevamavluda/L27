from playwright.sync_api import expect

from pages_demoqa.base_page import BasePage
from data import base_url_demoqa


class ButtonsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.btn_double_click_me = self.page.locator("#doubleClickBtn")
        self.btn_click_me = self.page.get_by_role("button", name="Click Me", exact=True)
        self.click_message = self.page.locator("#dynamicClickMessage")

    def open_page(self):
        self.page.goto(f"{base_url_demoqa}buttons")

    def assert_btn_text(self):
        text_btn = self.btn_double_click_me.inner_text()
        self.assert_subtext_in_text(text_btn, text="Double Click Me", msg="Кнопка")

    def click_btn_click_me(self):
        self.click(locator=self.btn_click_me)

    def message_click_me(self, message):
        expect(self.click_message).to_have_text(message)
        txt_btn = self.click_message.inner_text()
        return txt_btn


