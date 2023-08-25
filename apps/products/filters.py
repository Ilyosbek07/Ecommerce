from django_filters import FilterSet, RangeFilter, NumberFilter

from apps.products.models import ProductType


class ProductPriceFilter(FilterSet):
    price = RangeFilter()

    class Meta:
        model = ProductType
        fields = ['price']