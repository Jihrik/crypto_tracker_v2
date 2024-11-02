from django.urls import path, include
from ..views.assets import AssetView

urlpatterns = [
    path('assets/', AssetView.as_view(), name='asset-list'),
    path('assets/<int:pk>/', AssetView.as_view(), name='asset-detail'),
]