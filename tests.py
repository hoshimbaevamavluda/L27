from pages_demoqa.buttons_page import ButtonsPage
from pages_demoqa.text_box import TextBox


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

def test_27_03(page):
    t_box_page = TextBox(page)
    t_box_page.open_page()
    t_box_page.fill_full_name("Mavluda")
    name = t_box_page.input_value_name()
    t_box_page.fill_email("mava@mail.ru")
    email = t_box_page.input_value_email()
    print(f"Имя: {name}, Email: {email}")

def test_27_05(page):
    t_box_page = TextBox(page)
    t_box_page.open_page()
    print("inner_text:", repr(t_box_page.text_content_address()))
    print("text_content:", repr(t_box_page.inner_text_address()))
