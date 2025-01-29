def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера счёта"""

    return f"**{account_number[-4:]}"
