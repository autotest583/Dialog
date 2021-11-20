from selenium.webdriver.common.by import By

class MainPageLocators(): # класс описывает локаторы страницы авторизации
    login_button = (By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]') # кнопка "Login"

class EventsPageLocators(): # класс описывает локаторы страницы "События"
    # локаторы главной страницы "События"
    event_name = (By.CSS_SELECTOR, 'input[placeholder="Название"]') # поле поиска "Название"
    status = (By.CSS_SELECTOR, 'input[placeholder="Статус"]') # фильтр "Статус"
    checkbox_id = (By.XPATH, '//span[contains(@class,"el-checkbox__input")]') # чекбокс "Отобразить ID"
    checkbox_id_label = (By.CSS_SELECTOR, 'span[class="el-checkbox__label"]')  # лейбл чекбокса "Отобразить ID"
    add_button = (By.CSS_SELECTOR, 'button[class="el-button filter-item el-button--primary el-button--medium"]') # кнопка "Добавить"
    table = (By.CSS_SELECTOR, 'table[class="el-table__header"]') # таблица
    table_column_name = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[1]/div/text()') # колонка "Название"
    table_column_slug = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[2]/div/text()')  # колонка "Слаг"
    table_column_status = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[3]/div/text()')  # колонка "Статус"
    table_column_update = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[4]/div/text()')  # колонка "Обновлен"
    table_column_actions = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[5]/div')  # колонка "Действия"
    # локаторы формы создания ивента
    form_creation = (By.CSS_SELECTOR, 'div[aria-label="Создание"]') # форма "Создание ивента"
    header_creation = (By.CSS_SELECTOR, 'span[class="el-dialog__title"]') # заголовок
    close_creation = (By.CSS_SELECTOR, 'button[aria-label="Close"]') # крестик
    label_name = (By.CSS_SELECTOR, 'label[for="name"]') # лейбл "Название"
    label_slug = (By.CSS_SELECTOR, 'label[for="slug"]') # лейбл "Слаг"
    label_status = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/label/text()') # лейбл "Статус"
    field_name = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/input')  # поле "Название"
    field_slug = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/input')  # поле "Слаг"
    field_status = (By.CSS_SELECTOR, 'input[placeholder="Please select"]')  # поле "Статус"
    button_cancel = (By.CSS_SELECTOR, 'button[class="el-button el-button--default el-button--medium"]') # кнопка "Cancel"
    button_confirm = (By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]') # кнопка "Confirm"
    err_text = (By.XPATH, '//div[contains(text(),"Необходимо название")]') # ошибка поля "Название"

class CampaignsPageLocators(): # класс описывает локаторы страницы "Кампании"
    campaign_name = (By.CSS_SELECTOR, 'input[placeholder="Название"]') # поле поиска "Название"
    campaign_tags = (By.CSS_SELECTOR, 'input[placeholder="Тэги"]')  # поле поиска "Тэги"
    status = (By.CSS_SELECTOR, 'input[placeholder="Статус"]') # фильтр "Статус"
    channel = (By.CSS_SELECTOR, 'input[placeholder="Канал"]')  # фильтр "Канал"
    type = (By.CSS_SELECTOR, 'input[placeholder="Тип"]')  # фильтр "Тип"
    checkbox_id = (By.CSS_SELECTOR, 'span[class="el-checkbox__input"]') # чекбокс "Отобразить ID"
    checkbox_id_label = (By.CSS_SELECTOR, 'span[class="el-checkbox__label"]')  # лейбл чекбокса "Отобразить ID"
    add_button = (By.CSS_SELECTOR, 'button[class="el-button filter-item el-button--primary el-button--medium"]') # кнопка "Добавить"
    table = (By.CSS_SELECTOR, 'table[class="el-table__header"]') # таблица
    table_column_type = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[1]/div/text()')  # колонка "Тип"
    table_column_tags = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[2]/div')  # колонка "Тэги"
    table_column_channel = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[3]/div')  # колонка "Канал"
    table_column_name = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[4]/div/text()')  # колонка "Название"
    table_column_in = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[5]/div/text()')  # колонка "Отправится в"
    table_column_status = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[6]/div')  # колонка "Статус"
    table_column_update = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[7]/div/text()')  # колонка "Обновлен"
    table_column_actions = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[8]/div')  # колонка "Действия"

class SegmentsPageLocators(): # класс описывает локаторы страницы "Сегменты"
    segment_name = (By.CSS_SELECTOR, 'input[placeholder="Название"]') # поле поиска "Название"
    segment_tags = (By.CSS_SELECTOR, 'input[placeholder="Тэги"]')  # поле поиска "Тэги"
    status = (By.CSS_SELECTOR, 'input[placeholder="Статус"]') # фильтр "Статус"
    checkbox_id = (By.CSS_SELECTOR, 'span[class="el-checkbox__inner"]') # чекбокс "Отобразить ID"
    checkbox_id_label = (By.CSS_SELECTOR, 'span[class="el-checkbox__label"]')  # лейбл чекбокса "Отобразить ID"
    add_button = (By.CSS_SELECTOR, 'button[class="el-button filter-item el-button--primary el-button--medium"]') # кнопка "Добавить"
    table = (By.CSS_SELECTOR, 'table[class="el-table__header"]') # таблица
    table_column_tags = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[1]/div')  # колонка "Тэги"
    table_column_name = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[2]/div/text()')  # колонка "Название"
    table_column_status = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[3]/div/text()')  # колонка "Статус"
    table_column_update = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[4]/div/text()')  # колонка "Обновлен"
    table_column_actions = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[5]/div')  # колонка "Действия"

class TemplatesPageLocators(): # класс описывает локаторы страницы "Шаблоны"
    template_name = (By.CSS_SELECTOR, 'input[placeholder="Название"]') # поле поиска "Название"
    template_tags = (By.CSS_SELECTOR, 'input[placeholder="Тэги"]')  # поле поиска "Тэги"
    status = (By.CSS_SELECTOR, 'input[placeholder="Статус"]') # фильтр "Статус"
    channel = (By.CSS_SELECTOR, 'input[placeholder="Канал"]')  # фильтр "Канал"
    checkbox_id = (By.CSS_SELECTOR, 'span[class="el-checkbox__input"]') # чекбокс "Отобразить ID"
    checkbox_id_label = (By.CSS_SELECTOR, 'span[class="el-checkbox__label"]')  # лейбл чекбокса "Отобразить ID"
    add_button = (By.CSS_SELECTOR, 'button[class="el-button filter-item el-button--primary el-button--medium"]') # кнопка "Добавить"
    table = (By.CSS_SELECTOR, 'table[class="el-table__header"]') # таблица
    table_column_channel = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[1]/div/text()')  # колонка "Канал"
    table_column_tags = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[2]/div')  # колонка "Тэги"
    table_column_name = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[3]/div/text()')  # колонка "Название"
    table_column_status = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[4]/div/text()')  # колонка "Статус"
    table_column_update = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[5]/div/text()')  # колонка "Обновлен"
    table_column_actions = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[2]/div[2]/table/thead/tr/th[6]/div')  # колонка "Действия"

class StatisticsPageLocators(): # класс описывает локаторы страницы "Статистика"
    left_block = (By.CSS_SELECTOR, 'div[class="el-card box-card is-always-shadow"]')  # левый блок
    right_block = (By.CSS_SELECTOR, 'div[class="el-table el-table--fit el-table--border el-table--enable-row-hover el-table--enable-row-transition el-table--medium"]')  # правый блок

class UsersPageLocators(): # класс описывает локаторы страницы "Пользователи"
    user_data = (By.CSS_SELECTOR, 'input[placeholder="email, телефон, id lms, id NS"]')  # поле поиска