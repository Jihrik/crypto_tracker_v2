from django.core.exceptions import ValidationError
from django.db import models
from ..managers.wallet import WalletManager

class Wallet(models.Model):
    objects = WalletManager()

    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        from ..models.wallet_asset import WalletAsset

        asset_in_wallet = WalletAsset.objects.filter(wallet=self)
        if asset_in_wallet.exists():
            raise ValidationError(
                f"Cannot delete wallet when there are assets inside: {[str(asset) for asset in asset_in_wallet]}"
            )
        super().delete(*args, **kwargs)

