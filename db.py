import sqlite3 # Импорт модуля для работы с SQLite

def inserting_to_db(data): # Функция для вставки данных
    try:
        conn = sqlite3.connect("parsed_data.db") # Подключение к БД
        cursor = conn.cursor()
        print("Подключение к базе данных успешно!") # Сообщение в случае успешного подключения к  БД

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS parsed_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT NOT NULL,
                value TEXT
            )
        ''')
        print("Таблица успешно создана или уже существует!") # Сообщение в случае наличия существующего файла БД

        for key, value in data.items():
            if ":" in key:
                key_part = key.split(":")[0].strip()
                value_part = ":".join(key.split(":")[1:]).strip()
            else:
                key_part = key.strip()
                value_part = value.strip()

            cursor.execute("SELECT 1 FROM parsed_data WHERE key = ?", (key_part,))
            exists = cursor.fetchone()

            if not exists: 
                cursor.execute('INSERT INTO parsed_data (key, value) VALUES (?, ?)', (key_part, value_part))



        conn.commit() # Сохранение изменений в БД

    except Exception as e: # Сообщение об ошибке
        print(f"Ошибка при работе с базой данных: {e}")

    finally:

        conn.close() # Закрытие соединения с БД
