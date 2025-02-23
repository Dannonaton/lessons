import json
import os.path


def check_operations_file(path) -> list:
    """Функция, принимает на вход json file и проверяет его"""
    if not os.path.isfile(path) or os.path.getsize(path) == 0:
        return []
    with open(path, 'r', encoding='utf-8') as file:
        transaction_file = json.load(file)
        if not isinstance(transaction_file, list):
            return []
        else:
            return transaction_file

