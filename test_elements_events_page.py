from pages.main_page import MainPage
from pages.events_page import EventsPage
import time

def test_elements_events_page(browser): # тест на проверку наличия элементов страницы "События"
    page_home = MainPage(browser, MainPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home.open()  # открываем страницу авторизации
    page_home.go_to_campaigns_page() # выполняем метод страницы — переходим на страницу кампаний
    page_events = EventsPage(browser, EventsPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_events.open() # открываем страницу событий
    page_events.assert_event_name() # проверяем, что на странице присутствует поле поиска "Название"
    page_events.assert_status() # проверяем, что на странице присутствует фильтр по статусу
    page_events.assert_checkbox_id() # проверяем, что на странице присутствует чекбокс "Отобразить ID"
    page_events.assert_checkbox_id_label()  # проверяем, что на странице присутствует лейбл с наименованием "Отобразить ID"
    page_events.assert_button() # проверяем, что на странице присутствует кнопка "Добавить"
    page_events.assert_table() # проверяем, что на странице присутствует таблица
    page_events.assert_table_column_name() # проверяем, что на странице присутствует колонка с наименованием "Название"
    page_events.assert_table_column_slug()  # проверяем, что на странице присутствует колонка с наименованием "Слаг"
    page_events.assert_table_column_status()  # проверяем, что на странице присутствует колонка с наименованием "Статус"
    page_events.assert_table_column_update()  # проверяем, что на странице присутствует колонка с наименованием "Обновлен"
    page_events.assert_table_column_actions()  # проверяем, что на странице присутствует колонка с наименованием "Действия"
    page_events.events_checkbox_click() # клик по чекбоксу "Отобразить ID"
    page_events.events_checkbox_active() # проверяем, что чекбокс "Отобразить ID" активен