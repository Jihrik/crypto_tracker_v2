import requests
import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

from api.coingecko_api.models.coin_tickers import CoinTickers

def fetch_price(coin_id: str):
    ticker = coin_id
    print(f'ticker in fetch_price method() {ticker}')
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=' + coin_id + '&vs_currencies=usd'
    headers = {
        "accept": "application/json",
        "x-cg-pro-api-key": "CG-aGqP8kSdMduCKaAM3rmqwfZS\t"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        price = response.json()
        return price[ticker]['usd']
    else:
        # TODO after all tests remove comments here and in Assets overwiev line 24 show_assets
        price = 0.1
        print(response.text)
        print(f'failed to retrieve data from API. {coin_id.title()} price was set to 0.')
        return price


def get_available_coin_tickers():

    url = "https://api.coingecko.com/api/v3/simple/supported_vs_currencies"
    headers = {
        "accept": "application/json",
        "x-cg-pro-api-key": "CG-aGqP8kSdMduCKaAM3rmqwfZS"
    }
    response = requests.get(url, headers=headers)
    ticker_list = response.json()
    ticker_list = response.text.split('","')

    return ticker_list


def get_coin_data():
    url = "https://api.coingecko.com/api/v3/coins/list"

    headers = {
        "accept": "application/json",
        "x-cg-pro-api-key": "CG-aGqP8kSdMduCKaAM3rmqwfZS"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()


def save_to_json():
    data = get_available_coin_tickers()
    if data:
        json_object = json.dumps(data, indent=4)
        with open('available_coin_data.json', "w") as outfile:
            outfile.write(json_object)


def save_coin_data():
    data = get_coin_data()
    if data:
        for asset in data:
            CoinTickers.objects.create(asset_id=asset['id'], symbol=asset['symbol'], name=asset['name'])
