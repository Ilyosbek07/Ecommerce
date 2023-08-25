from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.products.choices import CURRENCY
from apps.company.models import CompanyProfile
from apps.products.validators import validate_rebate_time
from apps.users.models import User


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
    sub_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='extra_category',
        null=True,
        blank=True
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
    company_profile = models.ForeignKey(
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
    extra_info = models.ManyToManyField(
        ExtraInfo,
        related_name='extra_info'
    )
    name = models.CharField(max_length=55)
    is_shipping_free = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class WholeSale(BaseModel):
    product = models.ForeignKey(
        Product,
        related_name='product_extra_info',
        on_delete=models.CASCADE
    )
    product_from = models.IntegerField()
    product_to = models.IntegerField()
    price = models.DecimalField(max_digits=18, decimal_places=2, validators=[MinValueValidator(0)])
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'WholeSale {self.product_from} - {self.product_to}'

    class Meta:
        verbose_name = _('WholeSale')
        verbose_name_plural = _('WholeSales')


class ProductColor(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product Color")
        verbose_name_plural = _("Products Colors")


class ProductType(BaseModel):
    product = models.ForeignKey(
        to="Product", on_delete=models.CASCADE, related_name="stock"
    )
    color = models.ForeignKey(
        to="ProductColor",
        on_delete=models.SET_NULL,
        related_name="product_stocks",
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        _("Narx"), max_digits=18, decimal_places=2, validators=[MinValueValidator(0)]
    )
    sale_price = models.DecimalField(
        _("Chegirma narxi"), max_digits=18, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)]
    )
    currency = models.CharField(max_length=11, choices=CURRENCY.choices, default=CURRENCY.UZB)
    in_stock = models.PositiveIntegerField(_("Mahsulot soni"), default=0)

    class Meta:
        verbose_name = _("Product type")
        verbose_name_plural = _("Products type")


class Review(BaseModel):
    user = models.ForeignKey(
        User,
        related_name='user_review',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='product_review',
        on_delete=models.CASCADE
    )
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )
    msg = models.TextField()

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Rebate(BaseModel):
    category = models.ManyToManyField(
        Category,
        related_name='rebate_category',
    )
    discount_percent = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)
    ])
    until_time = models.DateTimeField(validators=[validate_rebate_time])

    def __str__(self):
        return f'Rebase {self.pk}'

    class Meta:
        verbose_name = 'Rebate'
        verbose_name_plural = 'Rebates'
