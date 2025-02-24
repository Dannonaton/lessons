import json
import os

from src.logger import get_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, '../logs', 'utils.log')
logger = get_logger('utils.log', file_path_1)


def check_operations_file(path) -> list:
    """Функция, принимает на вход json file и проверяет его"""
    try:
        logger.info(f'Запущена функция {check_operations_file.__name__} и ожидает на вход JSON файл')
        with open(path, 'r', encoding='utf-8') as file:
            transaction_file = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        logger.error(f'Произошла ошибка типа {FileNotFoundError}, {json.JSONDecodeError}')
        return []

    if not isinstance(transaction_file, list):
        logger.error('Произошла ошибка, JSON-файл не принадлежит типу list')
        return []
    logger.info(f'Функция {check_operations_file.__name__} завершила работу')
    return transaction_file
