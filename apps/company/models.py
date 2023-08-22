from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User


class Country(BaseModel):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    flag = models.ImageField(upload_to='country')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class CompanyProfile(BaseModel):
    user = models.ForeignKey(
        User,
        related_name='company_user',
        on_delete=models.CASCADE
    )
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo')
    shipping_place = models.CharField(
        max_length=255,
        choices=[('WorldWide', 'WorldWide'), ('Local', 'Local')])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('CompanyProfile')
        verbose_name_plural = _('CompanyProfiles')


class CompanyVerification(BaseModel):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='company_ver')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.company.name

    class Meta:
        verbose_name = _('CompanyVerification')
        verbose_name_plural = _('CompanyVerifications')
