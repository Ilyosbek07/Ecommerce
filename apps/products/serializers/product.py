from django.db.models import Avg, Count
from rest_framework import serializers

from apps.company.serializers import CompanyProfileSerializer
from apps.products.models import Product, ProductType, Review, WholeSale
from apps.products.serializers.othres import ImageSerializer, BrandSerializer, CategorySerializer, FeatureSerializer, \
    WholeSaleSerializer


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = (
            'color',
            'price',
            'sale_price',
            'currency',
            'in_stock',
        )


class ProductRetrieveSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    features = FeatureSerializer(many=True)
    stock = ProductTypeSerializer(many=True)
    # company_profile = serializers.ListSerializer(allow_empty=True, allow_null=True)
    product_extra_info = WholeSaleSerializer(many=True, read_only=True)

    sold = serializers.SerializerMethodField()
    review_rating = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'stock',
            'name',
            'is_shipping_free',
            'product_extra_info',
            'brand',
            'category',
            'features',
            'image',
            'review_rating',
            'reviews_count',
            'sold',
            # 'company_profile',
            'created_at',
            'created_at',
            'updated_at',
        )

    def get_sold(self, obj):
        return 123

    def get_review_rating(self, obj):
        rating_avg = Review.objects.filter(product=obj).aggregate(Avg('rating'))['rating__avg']
        if rating_avg:
            return rating_avg
        return 0

    def get_reviews_count(self, obj):
        review_count = Review.objects.filter(product=obj).count()
        return review_count
    # def valida
    # def get_whole_sale(self, obj):
    #     all = WholeSale.objects.filter(product=obj)
    #     return all


class ProductListSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    features = FeatureSerializer(many=True)
    stock = ProductTypeSerializer(many=True)
    review_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'stock',
            'name',
            'is_shipping_free',
            'brand',
            'category',
            'features',
            'image',
            'review_rating',
            'created_at',
            'updated_at',
        )

    def get_review_rating(self, obj):
        rating_avg = Review.objects.filter(product=obj).aggregate(Avg('rating'))['rating__avg']
        if rating_avg:
            return rating_avg
        return 0
