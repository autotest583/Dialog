from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import EventsPageLocators

class EventsPage(BasePage):

    url = "https://nsstage.skillbox.ru/#/events/index"

    def assert_event_name(self): # метод реализует проверку наличия элемента "Название"
        assert self.is_element_present(*EventsPageLocators.event_name), "Event name is not presented"

    def assert_status(self): # метод реализует проверку наличия элемента "Статус"
        assert self.is_element_present(*EventsPageLocators.status), "Status is not presented"

    def assert_checkbox_id(self): # метод реализует проверку наличия элемента "Отобразить ID"
        assert self.is_element_present(*EventsPageLocators.checkbox_id), "Checkbox id is not presented"

    def assert_checkbox_id_label(self): # метод реализует проверку лейбла чекбокса "Отобразить ID"
        checkbox_id_label = self.browser.find_element(*EventsPageLocators.checkbox_id_label).text
        assert checkbox_id_label == " Отобразить ID ", "Label Отобразить ID is not presented"

    def assert_button(self): # метод реализует проверку наличия элемента "кнопка Добавить"
        assert self.is_element_present(*EventsPageLocators.add_button), "Button add is not presented"

    def click_button(self): # метод реализует нажатие кнопки "Добавить"
        click_button = self.browser.find_element(*EventsPageLocators.add_button)
        click_button.click()

    def assert_table(self): # метод реализует проверку наличия элемента "Таблица"
        assert self.is_element_present(*EventsPageLocators.table), "Table is not presented"

    def assert_table_column_name(self): # метод реализует проверку колонки "Название"
        column_name = self.browser.find_element(*EventsPageLocators.table_column_name).text
        assert column_name == "Название", "Column name is not presented"

    def assert_table_column_slug(self): # метод реализует проверку колонки "Слаг"
        column_slug = self.browser.find_element(*EventsPageLocators.table_column_slug).text
        assert column_slug == "Слаг", "Column slug is not presented"

    def assert_table_column_status(self): # метод реализует проверку колонки "Статус"
        column_status = self.browser.find_element(*EventsPageLocators.table_column_status).text
        assert column_status == "Статус", "Column status is not presented"

    def assert_table_column_update(self): # метод реализует проверку колонки "Обновлен"
        column_update = self.browser.find_element(*EventsPageLocators.table_column_update).text
        assert column_update == "Обновлен", "Column update is not presented"

    def assert_table_column_actions(self): # метод реализует проверку колонки "Действия"
        column_actions = self.browser.find_element(*EventsPageLocators.table_column_actions).text
        assert column_actions == "Действия", "Column actions is not presented"

    def assert_form_creation(self): # метод реализует проверку наличия формы "Создание ивента"
        assert self.is_element_present(*EventsPageLocators.form_creation), "Form creation is not presented"

    def until_not_form_creation(self): # метод реализует проверку отсутствия формы "Создание ивента"
        assert self.is_disappeared(*EventsPageLocators.form_creation), "Form creation is presented"

    def assert_header_creation(self): # метод реализует проверку наличия заголовка "Создание"
        header_creation = self.browser.find_element(*EventsPageLocators.header_creation).text
        assert header_creation == "Создание", "Header is not presented"

    def assert_close_creation(self): # метод реализует проверку наличия элемента "Крестик"
        assert self.is_element_present(*EventsPageLocators.close_creation), "Close is not presented"

    def assert_label_name(self): # метод реализует проверку наличия лейбла "Название"
        label_name = self.browser.find_element(*EventsPageLocators.label_name).text
        assert label_name == "Название", "Label name is not presented"

    def assert_label_slug(self): # метод реализует проверку наличия лейбла "Слаг"
        label_slug = self.browser.find_element(*EventsPageLocators.label_slug).text
        assert label_slug == "Слаг", "Label slug is not presented"

    def assert_label_status(self): # метод реализует проверку наличия лейбла "Статус"
        label_status = self.browser.find_element(*EventsPageLocators.label_status).text
        assert label_status == "Статус", "Label status is not presented"

    def assert_field_name(self): # метод реализует проверку наличия поля "Название"
        assert self.browser.find_element(*EventsPageLocators.field_name), "Field name is not presented"

    def send_field_name(self, var): # метод реализует ввод значения в поле "Название"
        field_name = self.browser.find_element(*EventsPageLocators.field_name)
        field_name.send_keys(var)

    def assert_field_slug(self): # метод реализует проверку наличия поля "Слаг"
        assert self.browser.find_element(*EventsPageLocators.field_slug), "Field slug is not presented"

    def assert_field_status(self): # метод реализует проверку наличия поля "Статус"
        assert self.is_element_present(*EventsPageLocators.field_status), "Field status is not presented"

    def assert_button_cancel(self): # метод реализует проверку наличия кнопки "Cancel"
        assert self.is_element_present(*EventsPageLocators.button_cancel), "Button cancel is not presented"

    def assert_button_confirm(self): # метод реализует проверку наличия кнопки "Confirm"
        assert self.is_element_present(*EventsPageLocators.button_confirm), "Button confirm is not presented"

    def button_confirm_click(self): # метод реализует клик по кнопке "Confirm"
        self.browser.find_element(*EventsPageLocators.button_confirm).click()

    def button_cancel_click(self): # метод реализует клик по кнопке "Cancel"
        self.browser.find_element(*EventsPageLocators.button_cancel).click()

    def button_close_click(self): # метод реализует клик по кнопке "Крестик"
        self.browser.find_element(*EventsPageLocators.close_creation).click()

    def assert_err_text(self): # метод реализует проверку наличия ошибки "Необходимо название"
        assert self.browser.find_element(*EventsPageLocators.err_text)

    def events_url(self): # метод реализует проверку url страницы "События"
        url = self.browser.current_url
        assert url == "https://nsstage.skillbox.ru/#/events/index"

    def events_checkbox_click(self): # клик по чекбоксу
        self.browser.find_element(*EventsPageLocators.checkbox_id).click()

    def events_checkbox_active(self): # чекбокс активен
        checkbox = self.browser.find_element(*EventsPageLocators.checkbox_id).get_attribute("class")
        assert checkbox == "el-checkbox__input is-checked"

