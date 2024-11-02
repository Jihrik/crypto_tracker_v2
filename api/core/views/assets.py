from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from ..serializers.asset import AssetViewSerializer
from ..models.assets import Asset
from rest_framework.response import Response

class AssetView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        queryset = Asset.objects.all()
        serializer = AssetViewSerializer(queryset, many=True)
        return Response(serializer.data)
