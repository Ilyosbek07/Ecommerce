from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.company.models import Country, CompanyProfile
from apps.company.serializers import CompanyProfileSerializer, CompanyProfileCreateSerializer


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanyProfileCreateSerializer
    queryset = CompanyProfile.objects.all()
    permission_classes = [IsAuthenticated]

    # def get_object(self):
    #     country = generics.get_object_or_404(Country, pk=self.kwargs["pk"])
    #     return country

    # def get_queryset(self):
    #     company = self.get_object()
    #     return company.comments.all().visible()
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user.objects, content=self.get_object())
