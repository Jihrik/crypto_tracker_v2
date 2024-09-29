from django.urls import path, include
from ..views.wallets import WalletsView


urlpatterns = [
    path('wallets/', WalletsView.as_view({'get': 'list', 'post': 'create'}), name='wallet-list'),
    path('wallets/<int:pk>/', WalletsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='wallet-detail'),
]