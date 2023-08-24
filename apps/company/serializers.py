from rest_framework import serializers

from apps.company.models import Country, CompanyProfile, CompanyVerification


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'name',
            'city',
            'flag'
        )


class CompanyVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyVerification
        fields = (
            'company',
            'is_verified',
        )


class CompanyProfileSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = CompanyProfile
        fields = (
            'user',
            'country',
            'name',
            'logo',
            'shipping_place',
        )

class CompanyProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = (
            'user',
            'country',
            'name',
            'logo',
            'shipping_place',
        )
