import json
from json import JSONDecodeError


def check_operations_file(file_json) -> list:
    """Функция, принимает на вход json file и проверяет его"""
    try:
        with open(file_json) as file:
            try:
                transaction = json.load(file)
            except JSONDecodeError:
                print('Ошибка файла с транзакциями')
                return []
        if not isinstance(transaction, list):
            print('Список транзакции пуст')
            return []
        print('Создан список словарей с данными о фин опер')
        print(transaction)
        return transaction
    except FileNotFoundError:
        print('Файл не найден')
        return []
