from pages.main_page import MainPage
from pages.events_page import EventsPage
from pages.base_page import BasePage

# переменная для поля "Название"
randomname = BasePage.random_str(2)

def test_events_create(browser): # тест на проверку создания ивента
    page_home = MainPage(browser, MainPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home.open()  # открываем страницу авторизации
    page_home.go_to_campaigns_page() # выполняем метод страницы — переходим на страницу кампаний
    page_events = EventsPage(browser, EventsPage.url) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_events.open() # открываем страницу событий
    page_events.click_button() # нажимаем на кнопку "Добавить"
    page_events.send_field_name(randomname) # ввод значения в поле "Название"
    page_events.button_confirm_click() # нажимаем на кнопку "Confirm"
    page_events.refresh()  # обновляем страницу
    page_events.until_not_form_creation()  # проверяем, что форма "Создание ивента" отсутствует
    page_events.events_url()  # проверяем, что текущий url содержит /#/events/index