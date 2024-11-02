import time
import requests
from decimal import Decimal
from api.core.models.assets import Asset

def fetch_price(coin_id: str):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd'
    headers = {
        "accept": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        price = data.get(coin_id, {}).get('usd')
        if price is not None:
            return price
    elif response.status_code == 429:
        print(response.text)
        time.sleep(120)
        return fetch_price(coin_id)


def get_price():
    coin_list = Asset.objects.filter(current_price__isnull=True)
    for coin in coin_list:
        price = fetch_price(coin.coingecko_id)
        if price is not None:
            coin.current_price = Decimal(price)
            print(coin.id, coin.current_price)
            coin.save()