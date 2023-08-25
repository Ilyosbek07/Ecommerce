from rest_framework import serializers

from apps.products.models import Category, MainCategory, Brand, Feature, Image, ExtraInfo, Review, WholeSale, Rebate


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class WholeSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WholeSale
        fields = (
            'product',
            'product_from',
            'product_to',
            'price',
        )


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = (
            'name',
        )


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = (
            'name',
            'image'
        )


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'image',
            'is_main',
        )


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = (
            'name',
            'desc'
        )


class CategorySerializer(serializers.ModelSerializer):
    main_category = MainCategorySerializer()

    class Meta:
        model = Category
        fields = (
            'main_category',
            'name',
            'image',
        )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'user',
            'product',
            'rating',
            'msg'
        )


class RebateSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rebate
        fields = (
            'category',
            'discount_percent',
            'duration',
            'until_time',
            'created_at'
        )

    def get_duration(self, obj):
        duration = obj.until_time - obj.created_at
        return duration
