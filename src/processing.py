from typing import Any, Dict, List, Union

new_data = []

def filter_by_state(data: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, Union[str, None]]]:
    """ Функция, для сортировки по ключу """
    for i in data:
        if i["state"] == state:
            new_data.append(i)
    return new_data


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """ Функция, для сортировки списка по дате  """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)

