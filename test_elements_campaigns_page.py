from pages.main_page import MainPage
from pages.campaigns_page import CampaignsPage

def test_elements_campaigns_page(browser): # тест на проверку наличия элементов страницы "Кампании"
    page_home = MainPage(browser, MainPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home.open()  # открываем страницу авторизации
    page_home.go_to_campaigns_page() # выполняем метод страницы — переходим на страницу кампаний
    page_campaigns = CampaignsPage(browser, CampaignsPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_campaigns.open() # открываем страницу кампаний
    page_campaigns.assert_campaign_name() # проверяем, что на странице присутствует поле поиска "Название"
    page_campaigns.assert_campaign_tags()  # проверяем, что на странице присутствует поле поиска "Тэги"
    page_campaigns.assert_status() # проверяем, что на странице присутствует фильтр по статусу
    page_campaigns.assert_channel()  # проверяем, что на странице присутствует фильтр по каналу
    page_campaigns.assert_type()  # проверяем, что на странице присутствует фильтр по типу
    page_campaigns.assert_checkbox_id() # проверяем, что на странице присутствует чекбокс "Отобразить ID"
    page_campaigns.assert_checkbox_id_label()  # проверяем, что на странице присутствует лейбл с наименованием "Отобразить ID"
    page_campaigns.assert_button() # проверяем, что на странице присутствует кнопка "Добавить"
    page_campaigns.assert_table() # проверяем, что на странице присутствует таблица
    page_campaigns.assert_table_column_type() # проверяем, что на странице присутствует колонка с наименованием "Тип"
    page_campaigns.assert_table_column_tags() # проверяем, что на странице присутствует колонка с наименованием "Тэги"
    page_campaigns.assert_table_column_channel() # проверяем, что на странице присутствует колонка с наименованием "Канал"
    page_campaigns.assert_table_column_name() # проверяем, что на странице присутствует колонка с наименованием "Имя"
    page_campaigns.assert_table_column_in() # проверяем, что на странице присутствует колонка с наименованием "Отправится в"
    page_campaigns.assert_table_column_status() # проверяем, что на странице присутствует колонка с наименованием "Статус"
    page_campaigns.assert_table_column_update() # проверяем, что на странице присутствует колонка с наименованием "Обновлен"
    page_campaigns.assert_table_column_actions() # проверяем, что на странице присутствует колонка с наименованием "Действия"