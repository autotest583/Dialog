from pages.main_page import MainPage
from pages.events_page import EventsPage
import time

def test_events_create_validation(browser): # тест на проверку валидации элементов модального окна "Создание ивента"

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home = MainPage(browser, MainPage.url)

    # открываем страницу авторизации и переходим на страницу кампаний
    page_home.open()
    page_home.go_to_campaigns_page()

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_events = EventsPage(browser, EventsPage.url)

    # открываем страницу событий
    page_events.open()

    # нажимаем на кнопку "Добавить"
    page_events.click_button()

    # нажимаем на кнопку "Confirm" и проверяем отображение ошибки "Необходимо название"
    page_events.button_confirm_click()
    page_events.assert_err_text()

    # нажимаем на кнопку "Cancel" и бновляем страницу
    page_events.button_cancel_click()
    page_events.refresh()

    # проверяем, что форма "Создание ивента" отсутствует и, что текущий url содержит /#/events/index
    page_events.until_not_form_creation()
    page_events.events_url()

    # нажимаем на кнопку "Добавить" и на кнопку "Крестик"
    page_events.click_button()
    page_events.button_close_click()

    # обновляем страницу
    page_events.refresh()

    # проверяем, что форма "Создание ивента" отсутствует и, что текущий url содержит /#/events/index
    page_events.until_not_form_creation()
    page_events.events_url()