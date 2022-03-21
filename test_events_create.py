from pages.main_page import MainPage
from pages.events_page import EventsPage
from pages.base_page import BasePage

# переменная для поля "Название"
randomname = BasePage.random_str(2)

def test_events_create(browser): # тест на проверку создания ивента

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

    # ввод значения в поле "Название"
    page_events.send_field_name(randomname)

    # нажимаем на кнопку "Confirm"
    page_events.button_confirm_click()

    # обновляем страницу
    page_events.refresh()

    # проверяем, что форма "Создание ивента" отсутствует
    page_events.until_not_form_creation()

    # проверяем, что текущий url содержит /#/events/index
    page_events.events_url()