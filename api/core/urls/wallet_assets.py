from django.urls import path, include
from ..views.wallet_assets import WalletAssetView

urlpatterns = [
    path('wallets-assets/', WalletAssetView.as_view({'get': 'list', 'post': 'create'}), name='wallet-asset-list'),
    path('wallet-assets/<int:pk>/', WalletAssetView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='wallet-asset-detail'),
]