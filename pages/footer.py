from pages.base_page import BasePage

class Footer(BasePage): # класс описывает элементы футера

    url = "https://ria.ru"

    footer = ".footer.m-type-ria"  # блок footer
    footer_ria = ".footer__logos-ria" # логотип РИА НОВОСТИ
    footer_mia = ".footer__logos-mia" # логотип РОССИЯ СЕГОДНЯ
    block_social = ".footer__social-list .the-in-carousel__pack" # блок социальных сетей
    block_rubric = ".footer__rubric-list .the-in-carousel__pack" # блок рубрик
    block_client = ".footer__client-list .the-in-carousel__pack" # клиентский блок
    block_copyright = ".footer__copyright" # блок копирайт

    def assert_element(self, element):  # метод реализует проверку наличия элемента
        assert self.browser.find_element_by_css_selector(element), "Element is not presented"

    def move_element(self, element):  # прокрутка страницы до нужного элемента
        el = self.browser.find_element_by_css_selector(element)
        self.browser.execute_script("arguments[0].scrollIntoView();", el)

class FooterElements(Footer):

    social = " .footer__social-button"  # единица соц. сеть
    rubric = " .footer__rubric-item a"  # единица рубрика
    client = " .footer__client-item a"  # клиентская единица
    copyright = " .footer__copyright-col"  # единица копирайт
    version = "//div[contains(text(), ' Версия 2018.1 Beta')]" # версия
    certificate = "//div[contains(text(), ' Свидетельство о регистрации Эл № ФС77-57640')]"  # свидетельство
    contact = "//div[contains(text(), ' Главный редактор: ')]"  # текст из блока контакт

    def assert_element_len(self, element, int_el):  # метод реализует проверку кол-ва элементов
        len_el = self.browser.find_elements_by_css_selector(element)
        assert len(len_el) == int_el

    def title_element(self, element, int_el, title): # метод реализует проверку соц. сети по title
        el_unit = self.browser.find_elements_by_css_selector(element)
        el_attribute = el_unit[int_el].get_attribute("title")
        assert el_attribute == title, "Attribute contains another value"

    def text_element(self, element, int_el, text): # метод реализует проверку рубрики по тексту
        el_unit = self.browser.find_elements_by_css_selector(element)
        el_text = el_unit[int_el].text
        assert el_text == text, "Element contains another text"

    def click_element(self, element, int_el): # метод реализует клик по нужному элементу футера
        el_unit = self.browser.find_elements_by_css_selector(element)
        el_unit[int_el].click()

    def assert_elements(self, element, int_el):  # метод реализует проверку наличия элемента из списка
        el = self.browser.find_elements_by_css_selector(element)
        assert el[int_el]

    def assert_element_text(self, el_var):  # метод реализует поиск элемента по тексту
        el = self.browser.find_element_by_xpath(el_var)
        assert el, "Element is not presented"