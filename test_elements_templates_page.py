from pages.main_page import MainPage
from pages.templates_page import TemplatesPage

def test_elements_templates_page(browser): # тест на проверку наличия элементов страницы "Шаблоны"

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home = MainPage(browser, MainPage.url)

    # открываем страницу авторизации и переходим на страницу кампаний
    page_home.open()
    page_home.go_to_campaigns_page()

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_templates = TemplatesPage(browser, TemplatesPage.url)

    page_templates.open() # открываем страницу "Шаблоны"

    # проверяем элементы страницы
    page_templates.assert_template_name()
    page_templates.assert_template_tags()
    page_templates.assert_status()
    page_templates.assert_channel()
    page_templates.assert_checkbox_id()
    page_templates.assert_checkbox_id_label()
    page_templates.assert_button()
    page_templates.assert_table()
    page_templates.assert_table_column_channel()
    page_templates.assert_table_column_tags()
    page_templates.assert_table_column_name()
    page_templates.assert_table_column_status()
    page_templates.assert_table_column_update()
    page_templates.assert_table_column_actions()