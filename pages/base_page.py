from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string

class BasePage(): # метод-конструктор, который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what): # метод реализует перехват исключения
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def open(self): # метод реализует открытие страницы
        self.browser.get(self.url)

    def refresh(self): # метод реализует обновление страницы
        self.browser.refresh()

    @classmethod
    def random_str(cls, var):
        pp = ''.join(random.choices(string.ascii_letters + string.digits, k=(var)))
        return pp