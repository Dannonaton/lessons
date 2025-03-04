import json
import re

import pandas as pd


def load_transaction_file_from_json(file_path):
    """Загружаем список транзакции из JSON-файла"""
    with open(file_path, "r", encoding='utf-8') as file:
        return json.load(file)


def load_transaction_file_from_csv(file_path):
    """Загружаем список транзакции из CSV-файла"""
    df = pd.read_csv(file_path, encoding='utf-8', delimiter=';')
    return df.to_dict(orient='records')


def load_transaction_file_from_excel(file_path):
    """Загружаем список транзакции из Excel-файла"""
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')


def filter_transaction_by_status(transactions, status):
    """Фильтруем транзакции по статусу"""
    return [t for t in transactions if isinstance(t.get('state', ''), str) and t.get('state', '').lower(

    ) == status.lower()]


def sort_transaction_by_date(transactions, ascending=True):
    """Сортируем транзакции по дате"""
    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=not ascending)


def filter_transaction_by_currency(transactions, currency='руб.'):
    """Фильтруем транзакции по валюте"""
    return [t for t in transactions if currency in t.get('amount', '').lower()]


def filter_transaction_by_decription(transaction, search_string):
    """Фильтруем транзакции по строке в описании"""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [t for t in transaction if pattern.search(t.get('description', ''))]


def main():
    """Основная функция? которая взаимодействует с пользователем и обрабатывает транзакции"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню: ")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choise = input("Пожалуйста, выберите опцию: ")
    transactions = []

    if choise == "1":
        transactions = load_transaction_file_from_json("../lessons/data/operations.json")
        print("Для обработки выбран JSON-файл")
    elif choise == "2":
        transactions = load_transaction_file_from_csv("../lessons/data/transactions.csv")
        print("Для обработки выбран CSV-файл")
    elif choise == "3":
        transactions = load_transaction_file_from_excel("../lessons/data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл")
    else:
        print("Извините, некорректный ввод. Завершение работы программы.")
        return
    # print(transactions)
    filtering_operation = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        filters = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ")
        if filters.upper() in filtering_operation:
            transactions = filter_transaction_by_status(transactions, filters)
            print(f'Операции отфильтрованы по статусу "{filters.upper()}"')
            break
        else:
            print(f'Статус операции "{filters} не доступен"')

    if not transactions:
        print("Не найдено ни одной транзакции, подходящие под ваши условия фильтрации.")

    sort_choise = input("Отсортировать операции по дате (Да/Нет): ").strip().lower()
    if sort_choise == "да":
        order = input("Отсортировать по возрастанию или убыванию: ").strip().lower()
        transactions = sort_transaction_by_date(transactions, ascending=(order == "по возрастанию"))

    currency_choise = input("Выводить только рублевые транзакции? (Да/Нет): ")
    if currency_choise == "да":
        transactions = filter_transaction_by_currency(transactions)

    search_choice = (
        input("Отфильтровать список по определенному слову в описании? (Да/Нет): ").strip().lower()
    )
    if search_choice == "да":
        search_word = input("Введите слово для фильтрации: ")
        transactions = filter_transaction_by_decription(transactions, search_word)

    print("Распечатываю итоговый список транзакций...")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящие под ваши условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке {len(transactions)}")
        for transaction in transactions:
            print(f"{transaction.get('date', 'Неизвестная дата')} {transaction.get('description', 'Без описания')}")
            print(f"Сумма: {transaction.get('amount', 'Не указано')}")


if __name__ == '__main__':
    main()
