from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('api.core.urls.assets')),
    path('api/', include('api.core.urls.wallets')),
    path('api/', include('api.core.urls.wallet_assets')),
]
