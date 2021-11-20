from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import SegmentsPageLocators

class SegmentsPage(BasePage):

    url = "https://nsstage.skillbox.ru/#/segments/index"

    def assert_segment_name(self): # метод реализует проверку наличия элемента "Название"
        assert self.is_element_present(*SegmentsPageLocators.segment_name), "Segment name is not presented"

    def assert_segment_tags(self): # метод реализует проверку наличия элемента "Тэги"
        assert self.is_element_present(*SegmentsPageLocators.segment_tags), "Segment tags is not presented"

    def assert_status(self): # метод реализует проверку наличия элемента "Статус"
        assert self.is_element_present(*SegmentsPageLocators.status), "Status is not presented"

    def assert_checkbox_id(self): # метод реализует проверку наличия элемента "Отобразить ID"
        assert self.is_element_present(*SegmentsPageLocators.checkbox_id), "Checkbox is not presented"

    def assert_checkbox_id_label(self): # метод реализует проверку лейбла чекбокса "Отобразить ID"
        checkbox_id_label = self.browser.find_element(*SegmentsPageLocators.checkbox_id_label).text
        assert checkbox_id_label == " Отобразить ID ", "Label Отобразить ID is not presented"

    def assert_button(self): # метод реализует проверку наличия элемента "кнопка Добавить"
        assert self.is_element_present(*SegmentsPageLocators.add_button), "Button add is not presented"

    def assert_table(self): # метод реализует проверку наличия элемента "Таблица"
        assert self.is_element_present(*SegmentsPageLocators.table), "Table is not presented"

    def assert_table_column_tags(self): # метод реализует проверку колонки "Тэги"
        table_column_tags = self.browser.find_element(*SegmentsPageLocators.table_column_tags).text
        assert table_column_tags == "Тэги", "Column tags is not presented"

    def assert_table_column_name(self): # метод реализует проверку колонки "Название"
        table_column_name = self.browser.find_element(*SegmentsPageLocators.table_column_name).text
        assert table_column_name == "Название", "Column name is not presented"

    def assert_table_column_status(self): # метод реализует проверку колонки "Статус"
        table_column_status = self.browser.find_element(*SegmentsPageLocators.table_column_status).text
        assert table_column_status == "Статус", "Column status is not presented"

    def assert_table_column_update(self): # метод реализует проверку колонки "Обновлен"
        table_column_update = self.browser.find_element(*SegmentsPageLocators.table_column_update).text
        assert table_column_update == "Обновлен", "Column update is not presented"

    def assert_table_column_actions(self): # метод реализует проверку колонки "Действия"
        table_column_actions = self.browser.find_element(*SegmentsPageLocators.table_column_actions).text
        assert table_column_actions == "Действия", "Column actions is not presented"