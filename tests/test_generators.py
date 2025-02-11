import pytest

from src import generators


@pytest.mark.parametrize("transactions, currency", [
    ([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ], "USD")
])
def test_filter_by_currency(transactions, currency):
    filtered_transactions = generators.filter_by_currency(transactions, currency)
    assert next(filtered_transactions)["id"] == 939719570


@pytest.mark.parametrize('start, stop, expected', [(10, 12, ["0000 0000 0000 0010",
                                                             "0000 0000 0000 0011",
                                                             "0000 0000 0000 0012"]),
                                                   (5, 6, ["0000 0000 0000 0005",
                                                           "0000 0000 0000 0006"]),
                                                   (1000, 1002, ["0000 0000 0000 1000",
                                                                 "0000 0000 0000 1001",
                                                                 "0000 0000 0000 1002"])])
def test_card_number_generator(start, stop, expected):
    result = generators.card_number_generator(start, stop)
    assert next(result) == expected[0]
    assert next(result) == expected[1]


def test_card_number_generator_wrong_type() -> None:
    with pytest.raises(TypeError):
        next(generators.card_number_generator([1, 2, 3], 1))
    with pytest.raises(TypeError):
        next(generators.card_number_generator(5, "some_string"))


def test_card_number_generator_boundary_values() -> None:
    result_max = generators.card_number_generator(9999999999999998, 9999999999999999)
    assert next(result_max) == "9999 9999 9999 9998"
    assert next(result_max) == "9999 9999 9999 9999"


def test_card_number_generator_after_boundary_values() -> None:
    with pytest.raises(ValueError):
        next(generators.card_number_generator(10000000000000000, 10000000000000001))


def test_card_number_generator_wrong_start_stop() -> None:
    with pytest.raises(ValueError):
        next(generators.card_number_generator(7, 5))


def test_transaction_descriptions_exceptions() -> None:
    with pytest.raises(StopIteration):
        next(generators.transaction_descriptions([]))


def test_transaction_descriptions_wrong_type() -> None:
    with pytest.raises(TypeError):
        next(generators.transaction_descriptions(1))
    with pytest.raises(TypeError):
        next(generators.transaction_descriptions("some_string"))
