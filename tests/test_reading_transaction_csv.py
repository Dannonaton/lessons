from unittest.mock import patch

import pandas as pd

from src.reading_transactions_csv import get_data_transaction


@patch('pandas.read_csv')
def test_get_data_transaction(mock_read_csv):
    mock_data = pd.DataFrame({"id": ["1", "2", "3"], "Name": ["Sarah", "Mark", "John"]})
    mock_read_csv.return_value = mock_data

    result = get_data_transaction("fake")
    excpected = [
        {"id": "1", "Name": "Sarah"},
        {"id": "2", "Name": "Mark"},
        {"id": "3", "Name": "John"},
    ]
    assert result == excpected
