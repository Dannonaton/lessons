from datetime import datetime
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: Union[str]) -> str:
    """Функция, которая маскирует номер счета или карты"""

    split_input = type_and_number.split()
    if len(split_input) == 2:
        if split_input[0].lower() == "счет":
            new_input = "".join(split_input[-1])
            return f"{split_input[0]} {get_mask_account(new_input)}"
        else:
            new_input = "".join(split_input[-1])
            return f"{split_input[0]} {get_mask_card_number(new_input)}"
    elif len(split_input) == 3:
        new_input = "".join(split_input[-1])
        return f"{split_input[0]} {split_input[1]} {get_mask_card_number(new_input)}"
    else:
        return "Вы ввели неккоректные данные"


def get_date(user_date: Union[str]) -> str:
    """Функция получения даты в определенном формате и возвращения в формате ДД.ММ.ГГГГ
    с использованием Метода strptime() и strftime()"""

    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
