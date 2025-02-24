import os.path

from src.logger import get_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, '../logs', 'masks.log')
logger = get_logger('masks.log', file_path_1)


def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""
    logger.info(f'Запущена функция {get_mask_card_number.__name__} с аргументом {card_number}')
    if card_number == "":
        logger.error(f'Произошла ошибка типа {TypeError}: отсутствует аргумент ввода')
        raise TypeError('Отсутствует обязательный аргумент при вводе номера карты')
    elif len(card_number) >= 16:
        logger.error(f"Произошла ошибка типа {IndexError}: не соответствует длина строки аргументы ввода")
        raise IndexError("Не соответствует длина строки номера карты")
    logger.info(f'Функция завершила работу {get_mask_card_number.__name__} с аргументом {card_number}')
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера счёта"""
    logger.info(f'Запущена функция {get_mask_account.__name__} с аргументом {account_number}')
    if account_number == "":
        logger.error(f'Произошла ошибка типа {TypeError}: отсутствует аргумент ввода')
        raise TypeError('Отсутствует обязательный аргумент при вводе номера карты')
    elif len(account_number) >= 20:
        print(len(account_number))
        logger.error(f"Произошла ошибка типа {IndexError}: не соответствует длина строки аргументы ввода")
        raise IndexError("Не соответствует длина строки номера счёта")
    logger.info(f'Функция завершила работу {get_mask_account.__name__} с аргументом {account_number}')
    print(1)
    return f"**{account_number[-4:]}"
