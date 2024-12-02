# Импорт библиотек для работы с Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_captcha(driver, captcha_url_part, author_url_part): # Функция для ожидания CAPTCHA 

    while True: # Цикл пока нету CAPTCHA
        current_url = driver.current_url
        print(f"Текущий URL: {current_url}")

        if captcha_url_part in current_url: # В случае появления CAPTCHA
            print("Вы были переадресованы на страницу с CAPTCHA, пройдите её вручную")
            input("Нажмите Enter после прохождения CAPTCHA") # Ожидаем, пока пользователь нажмёт ENTER, что будет свидетельствовать о успешном прохождении CAPTCHA
        elif author_url_part in current_url: # Если мы находимся на странице автора
            print("CAPTCHA пройдена или отсутствует, идёт переадресация на целевую страницу")
            break
        else: # В случае, если находимся на иной странице
            print("Ждём редиректа на целевую страницу или на CAPTCHA")

def get_table(driver): # Функция для получения необходимых данных из HTML-разметки
    table = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//table[@width='580' and @cellspacing='0' and @cellpadding='3' and @style='border-spacing: 0px 2px;']")
        )
    )
    table_rows = table.find_elements(By.TAG_NAME, "tr") # Получаем все строки

    
    data = {}
    for row in table_rows: # В цикле проходим по всем строчкам таблицы
        columns = row.find_elements(By.TAG_NAME, "td")
        

        if len(columns) == 1 and columns[0].text.strip() == ",": # Пропускаем строки, состоящие из запятых
            continue

        if len(columns) > 2: # Если в строке больше двух столбцов
            key = columns[1].text.strip()  # Получаем ключ
            value = columns[2].text.strip() # Получаем значение
            if key and value:  
                data[key] = value # Добавляем данные в словарь data
    return data