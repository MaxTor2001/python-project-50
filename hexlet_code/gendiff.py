#!/usr/bin/env python3
import os
import argparse
import json

def generate_diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

        all_keys = set(data1.keys()).union(data2.keys())
        differences = {}

        for key in all_keys:
            if key not in data1:
                differences[key] = 'added'
            elif key not in data2:
                differences[key] = 'deleted'
            elif data1[key] != data2[key]:
                differences[key] = 'changed'
            else:
                differences[key] = 'unchanged'

        return differences

def parse_file(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON в файле {filename}: {e}")

def main():
    # Получение базовой директории
    base_dir = os.path.dirname(__file__)
    
    # Определяем пути к JSON-файлам
    file1 = os.path.join(base_dir, 'file1.json')
    file2 = os.path.join(base_dir, 'file2.json')

    # Вызываем функцию для вычисления различий
    diff_result = generate_diff(file1, file2)
    
    # Выводим различия между файлам
    if diff_result:
        for key, status in diff_result.items():
            print(f"Ключ '{key}' - {status}")

if __name__ == "__main__":
    main()