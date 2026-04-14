from pages_demoqa.data import base_url_demoqa


class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate_to_example(self, example_name: str):
        self.page.goto(base_url_demoqa)
        self.page.get_by_role("link", name=example_name).click()
        return self.page.url

    def assert_text_in_url_print(self, text_expected: str, msg: str = ""):
        assert text_expected in self.page.url, "Не та страница!"
        print(f"\n{msg}URL: {self.page.url}")

    @staticmethod
    def assert_subtext_in_text(subtext: str, text: str, msg: str = ""):
        assert subtext in text, f"{msg}'{text}' не содержит '{subtext}'"

    def click(self, locator, button: str = "left", click_count: int = 1,
              no_wait_after: bool = False) -> None:
        if isinstance(locator, str):
            locator = self.page.locator(locator)
        locator.click(button=button, click_count=click_count, no_wait_after=no_wait_after)

