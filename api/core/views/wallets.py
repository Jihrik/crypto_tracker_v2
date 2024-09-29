from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from ..serializers.wallet import WalletSerializer
from ..models.wallet import Wallet


class WalletsView(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()
