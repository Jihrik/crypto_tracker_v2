from __future__ import annotations

from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    symbol = models.CharField(max_length=100, unique=True)
    contract_address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    circulating_supply = models.DecimalField(max_digits=20, decimal_places=10)
    total_supply = models.DecimalField(max_digits=20, decimal_places=10)
    max_supply = models.DecimalField(max_digits=20, decimal_places=10)
    network = models.CharField(max_length=255)
    ath = models.DecimalField(max_digits=20, decimal_places=10)
    atl = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self) -> str:
        return self.name
