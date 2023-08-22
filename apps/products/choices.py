from django.db import models
from django.utils.translation import gettext_lazy as _


class CURRENCY(models.TextChoices):
    USA = "US", _("USD")
    UZB = "UZ", _("UZD")
    RUS = "RUS", _("RUBL")
