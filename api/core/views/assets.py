from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ..serializers.asset import AssetViewSerializer
from ..models.assets import Asset

class AssetView(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AssetViewSerializer
    queryset = Asset.objects.all()
