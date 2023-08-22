from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel, Company
from apps.products.choices import CURRENCY


class MainCategory(BaseModel):
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='main_category')

    def __str__(self):
        return self.name


class Category(BaseModel):
    main_category = models.ForeignKey(
        MainCategory,
        on_delete=models.CASCADE,
        related_name='main_category'
    )

    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='category')

    def __str__(self):
        return self.name


class Brand(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class Features(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name


class ExtraInfo(BaseModel):
    name = models.CharField(max_length=55)
    desc = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Image(BaseModel):
    image = models.ImageField(upload_to='product')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'Product {self.pk} image'


class WholeSale(BaseModel):
    product_from = models.IntegerField()
    product_to = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'WholeSale {self.product_from} - {self.product_to}'


class Product(BaseModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='prod_category'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='brand'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='company_prod'
    )
    image = models.ManyToManyField(
        Image,
        related_name='prod_image'
    )
    features = models.ManyToManyField(
        Features,
        related_name='features'
    )
    whole_sale = models.ManyToManyField(
        WholeSale,
        related_name='whole_sale'
    )
    extra_info = models.ManyToManyField(
        ExtraInfo,
        related_name='extra_info'
    )
    name = models.CharField(max_length=55)
    price = models.IntegerField(default=0)
    discount = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    discount_expire_date = models.DateTimeField()
    currency = models.CharField(max_length=11, choices=CURRENCY.choices,default=CURRENCY.UZB)
    is_shipping_free = models.BooleanField(default=False)
