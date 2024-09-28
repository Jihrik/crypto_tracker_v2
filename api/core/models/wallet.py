from __future__ import annotations

from django.core.exceptions import ValidationError
from django.db import models

from api.core.models.assets import Asset

class Wallet(models.Model):
    name = models.CharField(max_length=255, null=True)
    assets = models.ManyToManyField(Asset, related_name = 'Wallets')

    def __str__(self) -> str:
        return self.name

    def delete(self, *args, **kwargs):
        if self.assets.exists():
            raise ValidationError(f'Cannot delete wallet when there are assets inside: {self.assets}')
