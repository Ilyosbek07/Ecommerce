from django.contrib import admin

from apps.company.models import Country, CompanyProfile, CompanyVerification

admin.site.register(Country)
admin.site.register(CompanyProfile)
admin.site.register(CompanyVerification)