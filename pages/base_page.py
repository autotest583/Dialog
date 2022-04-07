class BasePage(): # метод-конструктор, который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): # метод реализует открытие страницы
        self.browser.get(self.url)

    def window(self, int_win): # метод реализует переключение вкладок
        window_name = self.browser.window_handles[int_win]
        self.browser.switch_to.window(window_name)

    def current_url(self, curr_url):  # метод реализует проверку url
        url = self.browser.current_url
        assert url == curr_url