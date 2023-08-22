from django.contrib import admin
from apps.common.models import Country, Company, CompanyVerification


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'shipping_place')
    list_filter = ('country', 'shipping_place')
    search_fields = ('name', 'country__name', 'shipping_place')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CompanyVerification)
class CompanyVerificationAdmin(admin.ModelAdmin):
    list_display = ('company', 'is_verified')
    list_filter = ('is_verified',)
    search_fields = ('company__name',)


admin.site.site_header = 'Your Admin Panel Header'
admin.site.site_title = 'Your Admin Panel Title'
