from pages_demoqa.buttons_page import ButtonsPage


def test_27_01(page):
    btn_page = ButtonsPage(page)
    btn_page.open_page()
    btn_page.assert_btn_text()
    print("Проверка отображения текста на кнопке. "
          "Прошла успешно ✅")

def test_27_02(page):
    btn_page = ButtonsPage(page)
    btn_page.open_page()
    btn_page.click_btn_click_me()
    message = "You have done a dynamic click"
    txt_message = btn_page.message_click_me(message)
    btn_page.assert_subtext_in_text(txt_message, message, msg="Текст ")
    print(f"Проверка отображения текста: {txt_message}."
          f" Прошла успешно ✅")


