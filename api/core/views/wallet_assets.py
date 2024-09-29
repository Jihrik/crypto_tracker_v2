from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from ..models.wallet_asset import WalletAsset
from ..serializers.wallet_asset import WalletAssetSerializer


class WalletAssetView(ModelViewSet):
    serializer_class = WalletAssetSerializer
    permission_classes = (AllowAny, )
    queryset = WalletAsset.objects.all()
