from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.products.choices import CURRENCY
from apps.company.models import CompanyProfile


class MainCategory(BaseModel):
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='main_category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('MainCategory')
        verbose_name_plural = _('MainCategories')


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

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Brand(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')


class Feature(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')


class ExtraInfo(BaseModel):
    name = models.CharField(max_length=55)
    desc = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('ExtraInfo')
        verbose_name_plural = _('ExtraInfo')


class Image(BaseModel):
    image = models.ImageField(upload_to='product')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'Product {self.pk} image'

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')


class WholeSale(BaseModel):
    product_from = models.IntegerField()
    product_to = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)

    def __str__(self):
        return f'WholeSale {self.product_from} - {self.product_to}'

    class Meta:
        verbose_name = _('WholeSale')
        verbose_name_plural = _('WholeSales')


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
    CompanyProfile = models.ForeignKey(
        CompanyProfile,
        on_delete=models.CASCADE,
        related_name='CompanyProfile_prod'
    )
    image = models.ManyToManyField(
        Image,
        related_name='prod_image'
    )
    features = models.ManyToManyField(
        Feature,
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
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    discount = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    discount_expire_date = models.DateTimeField()
    currency = models.CharField(max_length=11, choices=CURRENCY.choices, default=CURRENCY.UZB)
    is_shipping_free = models.BooleanField(default=False)
    sold = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=False)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
