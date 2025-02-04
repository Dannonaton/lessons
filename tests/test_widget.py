import pytest
from typing import Union
from src import widget


@pytest.mark.parametrize("type_and_number, expected", [
    ('Visa 7000792289606361', 'Visa 7000 79** **** 6361'),
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('Счет 64686473678894779589', 'Счет **9589')
])
def test_mask_account_card(type_and_number: Union[str], expected: Union[str]) -> None:
    assert widget.mask_account_card(type_and_number) == expected


@pytest.mark.parametrize("date, expected", [('2024-03-11T02:26:18.671407', '11.03.2024')])
def test_get_date(date: Union[str], expected: Union[str]) -> None:
    assert widget.get_date(date) == expected
