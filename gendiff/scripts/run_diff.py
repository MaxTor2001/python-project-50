from gendiff import generate_diff

def main():
    # Укажите пути к файлам JSON, которые хотите сравнить
    file1 = 'file1.json'
    file2 = 'file2.json'

    # Вызов функции для сравнения файлов
    diff_result = generate_diff(file1, file2)

    # Вывод результата сравнения
    print("Различия между файлами:")
    for key, status in diff_result.items():
        print(f"Ключ '{key}' {status}")

if __name__ == '__main__':
    main()