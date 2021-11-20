from pages.main_page import MainPage
from pages.events_page import EventsPage

def test_elements_events_create(browser): # тест на проверку наличия элементов модального окна "Создание ивента"
    page_home = MainPage(browser, MainPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home.open()  # открываем страницу авторизации
    page_home.go_to_campaigns_page() # выполняем метод страницы — переходим на страницу кампаний
    page_events = EventsPage(browser, EventsPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_events.open() # открываем страницу событий
    page_events.click_button() # нажимаем на кнопку "Добавить"
    page_events.assert_form_creation() # проверяем, что модальное окно отображается
    page_events.assert_header_creation() # проверяем, что в модальном окне присутствует заголовок "Создание"
    page_events.assert_close_creation() # проверяем, что в модальном окне присутствует кнопка "Крестик"
    page_events.assert_label_name() # проверяем, что в модальном окне присутствует лейбл "Название"
    page_events.assert_label_slug() # проверяем, что в модальном окне присутствует лейбл "Слаг"
    page_events.assert_label_status() # проверяем, что в модальном окне присутствует лейбл "Статус"
    page_events.assert_field_name() # проверяем, что в модальном окне присутствует поле "Название"
    page_events.assert_field_slug() # проверяем, что в модальном окне присутствует поле "Слаг"
    page_events.assert_field_status() # проверяем, что в модальном окне присутствует поле "Статус"
    page_events.assert_button_cancel() # проверяем, что в модальном окне присутствует кнопка "Cancel"
    page_events.assert_button_confirm() # проверяем, что в модальном окне присутствует кнопка "Confirm"