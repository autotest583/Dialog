from pages.footer import FooterElements
import time

def test_elements_footer(browser): # тест проверяет наличие элементов футера

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_ria = FooterElements(browser, FooterElements.url)

    # открываем главную страницу сайта РИА НОВОСТИ и прокручиваем ее до футера
    page_ria.open()
    page_ria.move_element(FooterElements.footer)

    # проверяем наличие основных блоков футера
    page_ria.assert_element(FooterElements.footer_ria)
    page_ria.assert_element(FooterElements.footer_mia)
    page_ria.assert_element(FooterElements.block_social)
    page_ria.assert_element(FooterElements.block_rubric)
    page_ria.assert_element(FooterElements.block_client)
    page_ria.assert_element(FooterElements.block_copyright)

    # проверяем наличие элементов блока "соц. сети"
    page_ria.assert_element_len(FooterElements.block_social + FooterElements.social, 9) # проверяем кол-во иконок соц. сетей
    page_ria.title_element(FooterElements.block_social + FooterElements.social, 0, "Сообщество ria Вконтакте") # проверяем наличие иконки Вконтакте
    page_ria.title_element(FooterElements.block_social + FooterElements.social, 1, "Группа ria в Одноклассниках")  # проверяем наличие иконки Одноклассники
    page_ria.title_element(FooterElements.block_social + FooterElements.social, 2, "ria в Яндекс.Дзен")  # проверяем наличие иконки Яндекс.Дзен
    page_ria.title_element(FooterElements.block_social + FooterElements.social, 3, "Сообщество ria")  # проверяем наличие иконки ria
    page_ria.title_element(FooterElements.block_social + FooterElements.social, 4, "Сообщество riaViber")  # проверяем наличие иконки riaViber
    page_ria.title_element(FooterElements.block_social + FooterElements.social, 5, "Канал ria в Telegram")  # проверяем наличие иконки Telegram
    page_ria.title_element(FooterElements.block_social + FooterElements.social, 6, "Новости ria в Twitter")  # проверяем наличие иконки Twitter
    page_ria.title_element(FooterElements.block_social + FooterElements.social, 7, "Срочные новости в Twitter riabreakingnews")  # проверяем наличие иконки riabreakingnews
    page_ria.title_element(FooterElements.block_social + FooterElements.social, 8, "Сообщество ria")  # проверяем наличие иконки ria (tiktok)

    # проверяем наличие элементов блока "рубрики"
    page_ria.assert_element_len(FooterElements.block_rubric + FooterElements.rubric, 14) # проверяем кол-во рубрик
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 0, "Политика") # проверяем наличие рубрики "Политика" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 1, "Общество")  # проверяем наличие рубрики "Общество" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 2, "Экономика")  # проверяем наличие рубрики "Экономика" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 3, "В мире")  # проверяем наличие рубрики "В мире" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 4, "Происшествия")  # проверяем наличие рубрики "Происшествия" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 5, "Спорт")  # проверяем наличие рубрики "Спорт" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 6, "Наука")  # проверяем наличие рубрики "Наука" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 7, "Культура")  # проверяем наличие рубрики "Культура" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 8, "Недвижимость")  # проверяем наличие рубрики "Недвижимость" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 9, "Религия")  # проверяем наличие рубрики "Религия" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 10, "Туризм")  # проверяем наличие рубрики "Туризм" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 11, "Радио")  # проверяем наличие рубрики "Радио" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 12, "Подкасты")  # проверяем наличие рубрики "Подкасты" по ее названию
    page_ria.text_element(FooterElements.block_rubric + FooterElements.rubric, 13, "Теги")  # проверяем наличие рубрики "Теги" по ее названию

    # проверяем наличие элементов клиентского блока
    page_ria.assert_element_len(FooterElements.block_client + FooterElements.client, 9) # проверяем кол-во клиентских разделов
    page_ria.text_element(FooterElements.block_client + FooterElements.client, 0, "Спецпроекты")  # проверяем наличие раздела "Спецпроекты"
    page_ria.text_element(FooterElements.block_client + FooterElements.client, 1, "Реклама")  # проверяем наличие раздела "Реклама"
    page_ria.text_element(FooterElements.block_client + FooterElements.client, 2, "Продукты и сервисы")  # проверяем наличие раздела "Продукты и сервисы"
    page_ria.text_element(FooterElements.block_client + FooterElements.client, 3, "Пресс-центр")  # проверяем наличие раздела "Пресс-центр"
    page_ria.text_element(FooterElements.block_client + FooterElements.client, 4, "Ria.ru в AppStore")  # проверяем наличие раздела "Ria.ru в AppStore"
    page_ria.text_element(FooterElements.block_client + FooterElements.client, 5, "Ria.ru в Google Play")  # проверяем наличие раздела "Ria.ru в Google Play"
    page_ria.text_element(FooterElements.block_client + FooterElements.client, 6, "Ria.ru APK")  # проверяем наличие раздела "Ria.ru APK"
    page_ria.text_element(FooterElements.block_client + FooterElements.client, 7, "RSS")  # проверяем наличие раздела "RSS"
    page_ria.text_element(FooterElements.block_client + FooterElements.client, 8, "Архив")  # проверяем наличие раздела "Архив"

    # проверяем наличие элементов блока копирайт
    page_ria.assert_element_len(FooterElements.block_copyright + FooterElements.copyright, 3) # проверяем кол-во блоков копирайта

    page_ria.assert_elements(FooterElements.block_copyright + FooterElements.copyright, 0)  # проверяем наличие блока с версией
    page_ria.assert_element_text(FooterElements.version)  # проверяем наличие текста "Версия 2018.1 Beta" (как пример)

    page_ria.assert_elements(FooterElements.block_copyright + FooterElements.copyright, 1)  # проверяем наличие блока со свидетельством
    page_ria.assert_element_text(FooterElements.certificate)  # проверяем наличие текста "Свидетельство о регистрации Эл № ФС77-57640" (как пример)

    page_ria.assert_elements(FooterElements.block_copyright + FooterElements.copyright, 2)  # проверяем наличие блока с контактной информацией
    page_ria.assert_element_text(FooterElements.contact)  # проверяем наличие текста "Главный редактор:" (как пример)

    time.sleep(2)