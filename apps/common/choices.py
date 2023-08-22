from django.db import models
from django.utils.translation import gettext_lazy as _


class QuantityType(models.TextChoices):
    kg = "Kg", _("KG")
    psc = "Psc", _("PSG")
    liter = "Liter", _("LITER")
