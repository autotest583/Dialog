from pages.main_page import MainPage
from pages.templates_page import TemplatesPage

def test_elements_templates_page(browser): # тест на проверку наличия элементов страницы "Шаблоны"
    page_home = MainPage(browser, MainPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home.open()  # открываем страницу авторизации
    page_home.go_to_campaigns_page() # выполняем метод страницы — переходим на страницу кампаний
    page_templates = TemplatesPage(browser, TemplatesPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_templates.open() # открываем страницу "Шаблоны"
    page_templates.assert_template_name() # проверяем, что на странице присутствует поле поиска "Название"
    page_templates.assert_template_tags()  # проверяем, что на странице присутствует поле поиска "Тэги"
    page_templates.assert_status() # проверяем, что на странице присутствует фильтр по статусу
    page_templates.assert_channel()  # проверяем, что на странице присутствует фильтр по каналу
    page_templates.assert_checkbox_id() # проверяем, что на странице присутствует чекбокс "Отобразить ID"
    page_templates.assert_checkbox_id_label()  # проверяем, что на странице присутствует лейбл с наименованием "Отобразить ID"
    page_templates.assert_button() # проверяем, что на странице присутствует кнопка "Добавить"
    page_templates.assert_table() # проверяем, что на странице присутствует таблица
    page_templates.assert_table_column_channel() # проверяем, что на странице присутствует колонка с наименованием "Канал"
    page_templates.assert_table_column_tags() # проверяем, что на странице присутствует колонка с наименованием "Тэги"
    page_templates.assert_table_column_name() # проверяем, что на странице присутствует колонка с наименованием "Название"
    page_templates.assert_table_column_status() # проверяем, что на странице присутствует колонка с наименованием "Статус"
    page_templates.assert_table_column_update() # проверяем, что на странице присутствует колонка с наименованием "Обновлен"
    page_templates.assert_table_column_actions() # проверяем, что на странице присутствует колонка с наименованием "Действия"