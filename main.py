




def main():
    """Основная функция? которая взаимодействует с пользователем и обрабатывает транзакции"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню: ")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choise = input("Пожалуйста, выберите опцию: ")
    transactions_file = []

    if choise == "1":
        print("Для обработки выбран JSON-файл")
    elif choise == "2":
        print("Для обработки выбран CSV-файл")
    elif choise == "3":
        print("Для обработки выбран XLSX-файл")
    else:
        print("Извините, некорректный ввод.")
        return

    filtering_operation = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        filters = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ")
        if filters.upper() in filtering_operation:
            print(f'Операции отфильтрованы по статусу "{filters.upper()}"')
            break
        else:
            print(f'Статус операции "{filters} не доступен"')




if __name__ == '__main__':
    main()