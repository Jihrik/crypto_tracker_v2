from rest_framework import serializers
from ..models.assets import Asset

class AssetViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = [
            "id",
            "coingecko_id",
            "name",
            "symbol",
            "contract_address",
            "current_price",
            "market_cap",
            "high_24h",
            "low_24h",
            "price_change_24h",
            "price_change_percentage_24h",
            "circulating_supply",
            "total_supply",
            "max_supply",
            "ath",
            "ath_date",
            "ath_change_percentage",
            "atl",
            "atl_date",
            "atl_change_percentage",
            "last_updated"
        ]

