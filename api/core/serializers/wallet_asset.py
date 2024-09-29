from rest_framework import serializers
from ..models.wallet_asset import WalletAsset


class WalletAssetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WalletAsset
        fields = [
            "id",
            "wallet",
            "asset",
            "amount"
        ]