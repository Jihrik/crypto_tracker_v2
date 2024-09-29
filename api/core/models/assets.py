from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=100, unique=True)
    contract_address = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    circulating_supply = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    total_supply = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    max_supply = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    network = models.CharField(max_length=255, null=True)
    ath = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    atl = models.DecimalField(max_digits=20, decimal_places=10, null=True)

    def __str__(self) -> str:
        return self.name