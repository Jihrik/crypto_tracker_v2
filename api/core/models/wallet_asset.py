from django.db import models
from ..models.assets import Asset
from ..models.wallet import Wallet


class WalletAsset(models.Model):

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=10)

    class Meta:
        unique_together = ('wallet', 'asset')

    def __str__(self) -> str:
        return f"{self.wallet.name} - {self.asset.symbol}: {self.amount}"
