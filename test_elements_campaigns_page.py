from pages.main_page import MainPage
from pages.campaigns_page import CampaignsPage

def test_elements_campaigns_page(browser): # тест на проверку наличия элементов страницы "Кампании"

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home = MainPage(browser, MainPage.url)

    # открываем страницу авторизации и переходим на страницу кампаний
    page_home.open()
    page_home.go_to_campaigns_page()

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_campaigns = CampaignsPage(browser, CampaignsPage.url)

    # открываем страницу кампаний
    page_campaigns.open()

    # проверяем элементы страницы
    page_campaigns.assert_campaign_name()
    page_campaigns.assert_campaign_tags()
    page_campaigns.assert_status()
    page_campaigns.assert_channel()

    page_campaigns.assert_type()
    page_campaigns.assert_checkbox_id()
    page_campaigns.assert_checkbox_id_label()
    page_campaigns.assert_button()

    page_campaigns.assert_table()
    page_campaigns.assert_table_column_type()
    page_campaigns.assert_table_column_tags()
    page_campaigns.assert_table_column_channel()

    page_campaigns.assert_table_column_name()
    page_campaigns.assert_table_column_in()
    page_campaigns.assert_table_column_status()
    page_campaigns.assert_table_column_update()
    page_campaigns.assert_table_column_actions()