import pytest
from playwright.sync_api import sync_playwright

from pages_demoqa.data import base_url_demoqa


@pytest.fixture
def page():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False)
        # print("Начало работы браузера")
        page_ = browser.new_page()
        page_.set_default_timeout(7000)
        page_.goto(base_url_demoqa)
        yield page_
        browser.close()
        # print("Завершение работы браузера")
