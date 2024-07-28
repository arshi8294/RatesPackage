import json
import requests


BASE_PATH = 'https://api.currencyfreaks.com/v2.0/rates/latest?apikey='

def get_rate(Api_key):
    """
    Send a http request to the exchange rate website
    :return: rates of USD
    """
    response = requests.get(BASE_PATH+Api_key)
    status = response.status_code
    if status == 200:
        data = json.loads(response.text)
        return data
    return None
