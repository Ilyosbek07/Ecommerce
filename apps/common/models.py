from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(BaseModel):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    flag = models.ImageField(upload_to='country')

    def __str__(self):
        return self.name


class Company(BaseModel):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logo')
    shipping_place = models.CharField(
        max_length=255,
        choices=[('WorldWide', 'WorldWide'), ('Local', 'Local')])

    def __str__(self):
        return self.name


class CompanyVerification(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,related_name='company_ver')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.company.name
