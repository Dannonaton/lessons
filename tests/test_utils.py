from src.utils import check_operations_file


def test_financial_transactions_nofile():
    assert check_operations_file('nofile') == []
