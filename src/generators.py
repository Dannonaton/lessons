

def filter_by_currency(transactions, currency):
    """Функция принимает на вход список со словарем и возвращает id операции"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions():
    pass

def card_number_generator():
    pass