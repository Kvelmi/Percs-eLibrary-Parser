def export_to_txt(data, filename="output.txt"): # Функция экспорта данных в .txt файл
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")
        print(f"Данные успешно экспортированы в файл {filename}")
    except Exception as e:
        print(f"Ошибка при экспорте в файл: {e}")
