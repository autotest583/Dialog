from pages.footer import FooterElements
import pytest
import time

@pytest.mark.parametrize('index, url', [
                (0, "https://vk.com/ria"),
                (1, "https://ok.ru/ria")
            ])
def test_social_url(browser, index, url): # тест проверяет возможность перехода на страницы соц. сетей

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_ria = FooterElements(browser, FooterElements.url)

    # открываем главную страницу сайта РИА НОВОСТИ и прокручиваем ее до футера
    page_ria.open()
    page_ria.move_element(FooterElements.footer)

    # проверяем переход и корректность перехода на страницу vk.com/ria
    page_ria.click_element(FooterElements.block_social + FooterElements.social, index)
    time.sleep(2)
    page_ria.window(1)
    time.sleep(2)
    page_ria.current_url(url)

@pytest.mark.parametrize('index, url', [
                (0, "https://ria.ru/politics/"),
                (1, "https://ria.ru/society/")
            ])
def test_rubric_url(browser, index, url): # тест проверяет возможность перехода на страницы соц. сетей

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_ria = FooterElements(browser, FooterElements.url)

    # открываем главную страницу сайта РИА НОВОСТИ и прокручиваем ее до футера
    page_ria.open()
    page_ria.move_element(FooterElements.footer)

    # проверяем переход и корректность перехода на страницу vk.com/ria
    page_ria.click_element(FooterElements.block_rubric + FooterElements.rubric, index)
    time.sleep(1)
    page_ria.current_url(url)

@pytest.mark.parametrize('index, url', [
                (0, "https://ria.ru/specialprojects/"),
                (3, "http://pressmia.ru/docs/about/index.html")
            ])
def test_client_url(browser, index, url): # тест проверяет возможность перехода на страницы соц. сетей

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_ria = FooterElements(browser, FooterElements.url)

    # открываем главную страницу сайта РИА НОВОСТИ и прокручиваем ее до футера
    page_ria.open()
    page_ria.move_element(FooterElements.footer)

    # проверяем переход и корректность перехода на страницу vk.com/ria
    page_ria.click_element(FooterElements.block_client + FooterElements.client, index)
    time.sleep(1)
    page_ria.current_url(url)