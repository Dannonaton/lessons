import csv

import pandas as pd



def get_data_transactions(operations_path):
    """Функция возвращает список словарей с данными о транзакциях csv"""
    with (open(operations_path, encoding='utf-8') as file):
        reader = pd.read_csv(file, delimiter=";")
        dict_trans = reader.to_dict(orient="records")
        dict_trans_str = [{str(k): v for k, v in d.items()} for d in dict_trans]
        print(dict_trans)
        print(dict_trans_str)


        return dict_trans, dict_trans_str





if __name__ == '__main__':
    list_file = get_data_transactions("../data/transactions_1.csv")
    print(list_file, sep="\n")