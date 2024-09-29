
from django.contrib import admin

from .models.assets import Asset
from .models.wallet import Wallet
from .models.wallet_asset import WalletAsset


admin.site.register(Asset)
admin.site.register(Wallet)
admin.site.register(WalletAsset)
