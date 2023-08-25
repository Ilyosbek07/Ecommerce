from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.products.filters import ProductPriceFilter
from apps.products.models import Product, ProductType
from apps.products.serializers.product import ProductRetrieveSerializer, ProductListSerializer, ProductTypeSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'brand', 'features']


class ProductTypeListAPIView(generics.ListAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['price']
    filter_class = ProductPriceFilter


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]
