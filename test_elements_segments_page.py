from pages.main_page import MainPage
from pages.segments_page import SegmentsPage

def test_elements_segments_page(browser): # тест на проверку наличия элементов страницы "Сегменты"

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home = MainPage(browser, MainPage.url)

    # открываем страницу авторизации и переходим на страницу кампаний
    page_home.open()
    page_home.go_to_campaigns_page()

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_segments = SegmentsPage(browser, SegmentsPage.url)

    # открываем страницу сегментов
    page_segments.open()

    # проверяем элементы страницы
    page_segments.assert_segment_name()
    page_segments.assert_segment_tags()
    page_segments.assert_status()
    page_segments.assert_checkbox_id()
    page_segments.assert_checkbox_id_label()
    page_segments.assert_button()
    page_segments.assert_table()
    page_segments.assert_table_column_tags()
    page_segments.assert_table_column_name()
    page_segments.assert_table_column_status()
    page_segments.assert_table_column_update()
    page_segments.assert_table_column_actions()