from django.urls import path

from apps.company.views import CompanyCreateView

urlpatterns = [
    path('create/', CompanyCreateView.as_view())
]
