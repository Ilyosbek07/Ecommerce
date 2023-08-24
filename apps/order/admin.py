from django.contrib import admin

from apps.order.models import Cart, Order

admin.site.register(Cart)
admin.site.register(Order)
