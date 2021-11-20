from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import CampaignsPageLocators

class CampaignsPage(BasePage):

    url = "https://nsstage.skillbox.ru/#/campaigns/index"

    def assert_campaign_name(self): # метод реализует проверку наличия элемента "Название"
        assert self.is_element_present(*CampaignsPageLocators.campaign_name), "Campaign name is not presented"

    def assert_campaign_tags(self): # метод реализует проверку наличия элемента "Тэги"
        assert self.is_element_present(*CampaignsPageLocators.campaign_tags), "Campaign tags is not presented"

    def assert_status(self): # метод реализует проверку наличия элемента "Статус"
        assert self.is_element_present(*CampaignsPageLocators.status), "Status is not presented"

    def assert_channel(self): # метод реализует проверку наличия элемента "Канал"
        assert self.is_element_present(*CampaignsPageLocators.channel), "Channel is not presented"

    def assert_type(self): # метод реализует проверку наличия элемента "Тип"
        assert self.is_element_present(*CampaignsPageLocators.type), "Type is not presented"

    def assert_checkbox_id(self): # метод реализует проверку наличия элемента "Отобразить ID"
        assert self.is_element_present(*CampaignsPageLocators.checkbox_id), "Checkbox is not presented"

    def assert_checkbox_id_label(self): # метод реализует проверку лейбла чекбокса "Отобразить ID"
        checkbox_id_label = self.browser.find_element(*CampaignsPageLocators.checkbox_id_label).text
        assert checkbox_id_label == " Отобразить ID ", "Label Отобразить ID is not presented"

    def assert_button(self): # метод реализует проверку наличия элемента "кнопка Добавить"
        assert self.is_element_present(*CampaignsPageLocators.add_button), "Button add is not presented"

    def assert_table(self): # метод реализует проверку наличия элемента "Таблица"
        assert self.is_element_present(*CampaignsPageLocators.table), "Table is not presented"

    def assert_table_column_type(self): # метод реализует проверку колонки "Тип"
        table_column_type = self.browser.find_element(*CampaignsPageLocators.table_column_type).text
        assert table_column_type == "Тип", "Column type is not presented"

    def assert_table_column_tags(self): # метод реализует проверку колонки "Тэги"
        table_column_tags = self.browser.find_element(*CampaignsPageLocators.table_column_tags).text
        assert table_column_tags == "Тэги", "Column tags is not presented"

    def assert_table_column_channel(self): # метод реализует проверку колонки "Канал"
        table_column_channel = self.browser.find_element(*CampaignsPageLocators.table_column_channel).text
        assert table_column_channel == "Канал", "Column channel is not presented"

    def assert_table_column_name(self): # метод реализует проверку колонки "Название"
        table_column_name = self.browser.find_element(*CampaignsPageLocators.table_column_name).text
        assert table_column_name == "Название", "Column name is not presented"

    def assert_table_column_in(self): # метод реализует проверку колонки "Отправится в"
        table_column_in = self.browser.find_element(*CampaignsPageLocators.table_column_in).text
        assert table_column_in == "Отправится в", "Column in is not presented"

    def assert_table_column_status(self): # метод реализует проверку колонки "Статус"
        table_column_status = self.browser.find_element(*CampaignsPageLocators.table_column_status).text
        assert table_column_status == "Статус", "Column status is not presented"

    def assert_table_column_update(self): # метод реализует проверку колонки "Обновлен"
        table_column_update = self.browser.find_element(*CampaignsPageLocators.table_column_update).text
        assert table_column_update == "Обновлен", "Column update is not presented"

    def assert_table_column_actions(self): # метод реализует проверку колонки "Действия"
        table_column_actions = self.browser.find_element(*CampaignsPageLocators.table_column_actions).text
        assert table_column_actions == "Действия", "Column actions is not presented"