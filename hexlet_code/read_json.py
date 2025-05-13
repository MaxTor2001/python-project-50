import json

def read_json(file_path):
    """Читает и парсит JSON файл, возвращает Python объекты."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)  # Парсинг JSON в Python объект
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON в файле {file_path}: {e}")

# Чтение данных из file1.json
data1 = read_json('file1.json')
print("Данные из file1.json:", data1)

# Чтение данных из file2.json
data2 = read_json('file2.json')
print("Данные из file2.json:", data2)