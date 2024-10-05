from django.db import models

from api.coingecko_api.managers.coin_tickers import CoinTickersManager


class CoinTickers(models.Model):
    objects = CoinTickersManager()

    asset_id = models.CharField(max_length=255, null=False)
    symbol = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)