#Импорт библиотек
from selenium_part import wait_for_captcha, get_table
from db import inserting_to_db
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import CAPTCHA_URL, AUTHOR_URL
from export import export_to_txt

def main():

    author_id = input("Введите user_id: ").strip() # Запрашиваем ID автора
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # Скрипт для проверки установки веб-драйвера
    driver.implicitly_wait(0.5)
    driver.get(f"https://www.elibrary.ru/author_profile.asp?id={author_id}") # Формирование ссылки со страницей автора
    wait_for_captcha(driver, CAPTCHA_URL, AUTHOR_URL) # Функция проверки CAPTCHA
    try:
        data = get_table(driver) # Получаем данные из таблицы
        if data: # Если данные найдены
            print("Основные показатели автора:")
            for key, value in data.items():
                print(f"{key}: {value}") 
            inserting_to_db(data)
            print("Данные были добавлены в БД") 
            export_to_txt(data, filename="parsed_data.txt")  # Выводим полученные данные и записываем их в БД и текстовый файл
        else: # Если данные не найдены
            print("Данные не найдены")
    except Exception as e: # Обработка ошибок
        screenshot_path = 'page_screenshot.png' # Скриншот страницы в случае ошибки парсинга
        driver.save_screenshot(screenshot_path)
        print(f"Ошибка при парсинге: {e}")
    finally:
        driver.quit() # Закрываем драйвер

if __name__ == "__main__":
    main()
