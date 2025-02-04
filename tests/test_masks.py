import pytest
from src import  masks



@pytest.mark.parametrize("date, expected", [
    ('7000791234566361', '7000 79** **** 6361'),
    ('1234567887654321', '1234 56** **** 4321'),
    ('7865273968278382', '7865 27** **** 8382')
])
def test_get_mask_card_number(date, expected):
    assert masks.get_mask_card_number(date) == expected

@pytest.mark.parametrize("date, expected", [
    ('73654108430135874305', '**4305'),
    ('7123131231313123123123', '**3123'),
    ('13123131231232134124234', '**4234')
])
def test_get_mask_account(date, expected):
    assert masks.get_mask_account(date) == expected

