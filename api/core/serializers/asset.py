from rest_framework import serializers
from ..models.assets import Asset


class AssetViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            "id",
            "name", 
            "symbol", 
            "contract_address",
            "price", 
            "circulating_supply",
            "total_supply",
            "max_supply",
            "network",
            "ath",
            "atl"
        ]