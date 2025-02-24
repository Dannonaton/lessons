import json
import os.path


def check_operations_file(path) -> list:
    """Функция, принимает на вход json file и проверяет его"""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            transaction_file = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

    if not isinstance(transaction_file, list):
        return []

    return transaction_file
