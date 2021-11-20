from pages.main_page import MainPage
from pages.segments_page import SegmentsPage

def test_elements_segments_page(browser): # тест на проверку наличия элементов страницы "Сегменты"
    page_home = MainPage(browser, MainPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home.open()  # открываем страницу авторизации
    page_home.go_to_campaigns_page() # выполняем метод страницы — переходим на страницу кампаний
    page_segments = SegmentsPage(browser, SegmentsPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_segments.open() # открываем страницу сегментов
    page_segments.assert_segment_name() # проверяем, что на странице присутствует поле поиска "Название"
    page_segments.assert_segment_tags() # проверяем, что на странице присутствует поле поиска "Тэги"
    page_segments.assert_status() # проверяем, что на странице присутствует фильтр по статусу
    page_segments.assert_checkbox_id() # проверяем, что на странице присутствует чекбокс "Отобразить ID"
    page_segments.assert_checkbox_id_label()  # проверяем, что на странице присутствует лейбл с наименованием "Отобразить ID"
    page_segments.assert_button() # проверяем, что на странице присутствует кнопка "Добавить"
    page_segments.assert_table() # проверяем, что на странице присутствует таблица
    page_segments.assert_table_column_tags() # проверяем, что на странице присутствует колонка с наименованием "Тэги"
    page_segments.assert_table_column_name() # проверяем, что на странице присутствует колонка с наименованием "Название"
    page_segments.assert_table_column_status() # проверяем, что на странице присутствует колонка с наименованием "Статус"
    page_segments.assert_table_column_update() # проверяем, что на странице присутствует колонка с наименованием "Обновлен"
    page_segments.assert_table_column_actions() # проверяем, что на странице присутствует колонка с наименованием "Действия"