from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import EventsPageLocators

class EventsPage(BasePage):
    def assert_event_name(self): # метод реализует проверку наличия элемента "Название"
        assert self.is_element_present(*EventsPageLocators.event_name), "Event name is not presented"

    def assert_event_name_placeholder(self): # метод реализует проверку плейсхолдера элемента "Название"
        event_name_placeholder = self.browser.find_element(*EventsPageLocators.event_name).get_attribute("placeholder")
        assert event_name_placeholder == "Название", "Placeholder 'Название' is not presented"

    def assert_status(self): # метод реализует проверку наличия элемента "Статус"
        assert self.is_element_present(*EventsPageLocators.status), "Status is not presented"

    def assert_filter_id(self): # метод реализует проверку наличия элемента "Отобразить ID"
        assert self.is_element_present(*EventsPageLocators.filter_id), "Filter id is not presented"

    def assert_button(self): # метод реализует проверку наличия элемента "кнопка Добавить"
        assert self.is_element_present(*EventsPageLocators.add_button), "Button add is not presented"

    def assert_table(self): # метод реализует проверку наличия элемента "Таблица"
        assert self.is_element_present(*EventsPageLocators.table), "Table is not presented"