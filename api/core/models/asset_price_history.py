from django.db import models

from api.core.models import Asset


class AssetPriceHistory(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=20, decimal_places=10)


    # TODO will need to set-up cleanup function for orphaned data rows as I don't want to have too many undeleted rows