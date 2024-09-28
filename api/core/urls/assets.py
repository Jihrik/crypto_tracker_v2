from django.urls import path, include
from ..views.assets import AssetView
urlpatterns = [
    path('assets/', AssetView.as_view({'get': 'list', 'post': 'create'}), name='asset-list'),
]