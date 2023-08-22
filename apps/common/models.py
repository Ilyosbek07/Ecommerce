from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.choices import QuantityType


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SendQuote(BaseModel):
    item = models.CharField(max_length=125)
    desc = models.TextField()
    quantity = models.DecimalField(default=0, decimal_places=2, max_digits=1000)
    quantity_type = models.CharField(max_length=15, choices=QuantityType.choices)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = _('SendQuote')
        verbose_name_plural = _('SendQuotes')
