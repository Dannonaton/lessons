import pandas as pd


def get_data_transaction(operations_path):
    """Функция возвращает список словарей с данными о транзакциях csv"""
    df = pd.read_csv(operations_path, encoding='utf-8', delimiter=';')
    dict_trans = df.to_dict(orient="records")
    return dict_trans



if __name__ == '__main__':
    list_file = get_data_transaction("../data/transactions.csv")
    print(*list_file, sep="\n")
