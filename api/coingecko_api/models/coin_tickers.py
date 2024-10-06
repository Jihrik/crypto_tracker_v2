from django.db import models
from django.views.generic.dates import timezone_today

from api.coingecko_api.managers.coin_tickers import CoinTickersManager


class CoinTickers(models.Model):
    objects = CoinTickersManager()

    symbol = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    asset_id = models.CharField(max_length=255, unique=True, null=False)
