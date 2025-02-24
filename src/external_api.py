import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def currency_convertor(transaction: dict) -> float:
    """Функция конвертации через внешний API"""
    amount = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    if code != 'RUB':
        url = f'https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}'
        payload = {}
        response = requests.get(url, headers={"apikey" : API_KEY}, data=payload)
        result = response.json()
        return round(result["result"], 2)
    else:
        return float(amount)
