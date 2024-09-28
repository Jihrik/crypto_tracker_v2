from __future__ import annotations

from django.contrib import admin

from .models.assets import Asset
from .models.wallet import Wallet

admin.site.register(Asset)
admin.site.register(Wallet)
