from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import TemplatesPageLocators

class TemplatesPage(BasePage):

    url = "https://nsstage.skillbox.ru/#/templates/index"

    def assert_template_name(self): # метод реализует проверку наличия элемента "Название"
        assert self.is_element_present(*TemplatesPageLocators.template_name), "Template name is not presented"

    def assert_template_tags(self): # метод реализует проверку наличия элемента "Тэги"
        assert self.is_element_present(*TemplatesPageLocators.template_tags), "Template tags is not presented"

    def assert_status(self): # метод реализует проверку наличия элемента "Статус"
        assert self.is_element_present(*TemplatesPageLocators.status), "Status is not presented"

    def assert_channel(self): # метод реализует проверку наличия элемента "Канал"
        assert self.is_element_present(*TemplatesPageLocators.channel), "Channel is not presented"

    def assert_checkbox_id(self): # метод реализует проверку наличия элемента "Отобразить ID"
        assert self.is_element_present(*TemplatesPageLocators.checkbox_id), "Checkbox is not presented"

    def assert_checkbox_id_label(self): # метод реализует проверку лейбла чекбокса "Отобразить ID"
        checkbox_id_label = self.browser.find_element(*TemplatesPageLocators.checkbox_id_label).text
        assert checkbox_id_label == " Отобразить ID ", "Label Отобразить ID is not presented"

    def assert_button(self): # метод реализует проверку наличия элемента "кнопка Добавить"
        assert self.is_element_present(*TemplatesPageLocators.add_button), "Button add is not presented"

    def assert_table(self): # метод реализует проверку наличия элемента "Таблица"
        assert self.is_element_present(*TemplatesPageLocators.table), "Table is not presented"

    def assert_table_column_channel(self): # метод реализует проверку колонки "Канал"
        table_column_channel = self.browser.find_element(*TemplatesPageLocators.table_column_channel).text
        assert table_column_channel == "Канал", "Column channel is not presented"

    def assert_table_column_tags(self): # метод реализует проверку колонки "Тэги"
        table_column_tags = self.browser.find_element(*TemplatesPageLocators.table_column_tags).text
        assert table_column_tags == "Тэги", "Column tags is not presented"

    def assert_table_column_name(self): # метод реализует проверку колонки "Название"
        table_column_name = self.browser.find_element(*TemplatesPageLocators.table_column_name).text
        assert table_column_name == "Название", "Column name is not presented"

    def assert_table_column_status(self): # метод реализует проверку колонки "Статус"
        table_column_status = self.browser.find_element(*TemplatesPageLocators.table_column_status).text
        assert table_column_status == "Статус", "Column status is not presented"

    def assert_table_column_update(self): # метод реализует проверку колонки "Обновлен"
        table_column_update = self.browser.find_element(*TemplatesPageLocators.table_column_update).text
        assert table_column_update == "Обновлен", "Column update is not presented"

    def assert_table_column_actions(self): # метод реализует проверку колонки "Действия"
        table_column_actions = self.browser.find_element(*TemplatesPageLocators.table_column_actions).text
        assert table_column_actions == "Действия", "Column actions is not presented"