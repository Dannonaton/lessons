import pandas as pd


def get_data_transaction(operation_path):
    """Функция возвращает список словарей с данными о транзакциях excel"""
    df = pd.read_excel(operation_path)
    dict_trans = df.to_dict(orient="records")
    return dict_trans

#
# if __name__ == '__main__':
#     operation_path = '../data/transactions_excel.xlsx'
#     list_trans = get_data_transaction(operation_path)
#     print(type(list_trans))
#     print(*list_trans, sep="\n")
