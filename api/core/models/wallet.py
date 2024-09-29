from django.core.exceptions import ValidationError
from django.db import models

from ..models.assets import Asset


class Wallet(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.assets.exists():
            raise ValidationError(
                f"Cannot delete wallet when there are assets inside: {self.assets}"
            )