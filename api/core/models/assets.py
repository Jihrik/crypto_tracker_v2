from django.db import models
from api.coingecko_api.models.coin_tickers import CoinTickers
from api.core.managers.asset import AssetManager


class Asset(models.Model):
    objects = AssetManager()

    coingecko_id = models.CharField(max_length=255, null=True, unique=True)

    contract_address = models.CharField(max_length=255, null=True)
    current_price = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    market_cap = models.DecimalField(max_digits=30, decimal_places=10, null=True)
    market_cap_rank = models.IntegerField(null=True)
    high_24h = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    low_24h = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    price_change_24h = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    price_change_percentage_24h = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    circulating_supply = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    total_supply = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    max_supply = models.DecimalField(max_digits=20, decimal_places=10, null=True)

    # ATH
    ath = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    ath_date = models.DateTimeField(null=True)
    ath_change_percentage = models.DecimalField(max_digits=10, decimal_places=5, null=True)

    # ATL
    atl = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    atl_date = models.DateTimeField(null=True)
    atl_change_percentage = models.DecimalField(max_digits=10, decimal_places=5, null=True)

    last_updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.coingecko_id

    @property
    def symbol(self):
        return self.coingecko_id.symbol

    @property
    def name(self):
        return self.coingecko_id.name