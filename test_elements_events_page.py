from pages.main_page import MainPage
from pages.events_page import EventsPage
import time

def test_elements_events_page(browser): # тест на проверку наличия элементов страницы "События"

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home = MainPage(browser, MainPage.url)

    # открываем страницу авторизации и переходим на страницу кампаний
    page_home.open()
    page_home.go_to_campaigns_page()

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_events = EventsPage(browser, EventsPage.url)

    # открываем страницу событий
    page_events.open()

    # проверяем элементы страницы
    page_events.assert_event_name()
    page_events.assert_status()
    page_events.assert_checkbox_id()
    page_events.assert_checkbox_id_label()
    page_events.assert_button()
    page_events.assert_table()
    page_events.assert_table_column_name()
    page_events.assert_table_column_slug()
    page_events.assert_table_column_status()
    page_events.assert_table_column_update()
    page_events.assert_table_column_actions()
    page_events.events_checkbox_click()
    page_events.events_checkbox_active()