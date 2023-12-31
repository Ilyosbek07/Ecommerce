from django.contrib import admin
from apps.products.models import (
    Product,
    ExtraInfo,
    MainCategory,
    Category,
    WholeSale,
    Image,
    Feature,
    Brand, ProductType, ProductColor, Review, Rebate
)

admin.site.register(Rebate)
admin.site.register(ProductType)
admin.site.register(ProductColor)
admin.site.register(Review)


class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(MainCategory, MainCategoryAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_category')
    list_filter = ('main_category',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Brand, BrandAdmin)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Feature, FeatureAdmin)


class ExtraInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')
    search_fields = ('name', 'desc')


admin.site.register(ExtraInfo, ExtraInfoAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'is_main')
    list_filter = ('is_main',)
    search_fields = ('image',)


admin.site.register(Image, ImageAdmin)


class WholeSaleAdmin(admin.ModelAdmin):
    list_display = ('product_from', 'product_to', 'price')


admin.site.register(WholeSale, WholeSaleAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand')
    list_filter = ('category', 'brand', 'features')
    search_fields = ('name',)
    filter_horizontal = ('image', 'features', 'extra_info')
    # readonly_fields = ('sold',)


admin.site.register(Product, ProductAdmin)
