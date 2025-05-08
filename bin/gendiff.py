#!/usr/bin/env python3

import argparse
import json


def parse_file(filename):
    """Парсит JSON-файл и возвращает данные."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return None  # Return None to explicitly indicate the error
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON в файле {filename}: {e}")
        return None  # Return None to explicitly indicate the error

def compare_json(data1, data2):
    """Сравнивает два словаря JSON и выводит различия."""
    differences = {}
    for key in set(data1.keys()).union(set(data2.keys())):  # Get all keys from both dictionaries
        if key in data1 and key not in data2:
            differences[key] = ('only in first file', data1[key])
        elif key not in data1 and key in data2:
            differences[key] = ('only in second file', data2[key])
        elif data1[key] != data2[key]:
            differences[key] = ('different values', (data1[key], data2[key]))
    return differences

def main():
    parser = argparse.ArgumentParser(
        description="Compares two JSON configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str, help="file1.json")
    parser.add_argument("second_file", type=str, help="file2.json")

    args = parser.parse_args()

    # Чтение и парсинг переданных файлов
    data1 = parse_file(args.first_file)
    data2 = parse_file(args.second_file)

    if data1 is not None and data2 is not None:
        # Compare the parsed data
        differences = compare_json(data1, data2)
        print("Различия между файлами:", differences)

if __name__ == "__main__":
    main()
